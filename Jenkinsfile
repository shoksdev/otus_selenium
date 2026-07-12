pipeline {
    agent any

    parameters {
        string(
            name: 'EXECUTOR_URL',
            defaultValue: 'http://selenoid:4444/wd/hub',
            description: 'URL адрес Executor (например: http://selenoid:4444/wd/hub)'
        )
        string(
            name: 'PRESTASHOP_URL',
            defaultValue: 'http://prestashop:80/',
            description: 'URL адрес PrestaShop (например: http://prestashop:80/)'
        )
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox'],
            description: 'Выберите браузер для запуска тестов'
        )
        choice(
            name: 'BROWSER_VERSION',
            choices: ['125.0', '127.0'],
            description: 'Выберите версию браузера для запуска тестов'
        )
        string(
            name: 'FLOW_COUNT',
            defaultValue: '4',
            description: 'Укажите количество потоков'
        )
        text(
            name: 'PYTEST_ARGS',
            defaultValue: '--alluredir allure-results --strict-markers --tb=short --verbose',
            description: 'Дополнительные аргументы для pytest'
        )
        booleanParam(
            name: 'RUN_LINT',
            defaultValue: false,
            description: 'Запускать ли линтер?'
        )
        booleanParam(
            name: 'GENERATE_ALLURE',
            defaultValue: true,
            description: 'Генерировать ли Allure отчет?'
        )
    }

    environment {
        VENV_PATH = "${WORKSPACE}/.venv"
        EXECUTOR_URL = "${params.EXECUTOR_URL}"
        PRESTASHOP_URL = "${params.PRESTASHOP_URL}"
        BROWSER = "${params.BROWSER}"
        BROWSER_VERSION = "${params.BROWSER_VERSION}"
        FLOW_COUNT = "${params.FLOW_COUNT}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "🔄 Клонирование репозитория..."
                checkout scm
            }
        }

        stage('Environment Info') {
            steps {
                echo "📋 Параметры сборки:"
                echo "   WORKSPACE: ${WORKSPACE}"
                echo "   EXECUTOR_URL: ${params.EXECUTOR_URL}"
                echo "   PRESTASHOP_URL: ${params.PRESTASHOP_URL}"
                echo "   BROWSER: ${params.BROWSER}"
                echo "   BROWSER_VERSION: ${params.BROWSER_VERSION}"
                echo "   FLOW_COUNT: ${params.FLOW_COUNT}"
                echo "   PYTEST_ARGS: ${params.PYTEST_ARGS}"
                echo "   RUN_LINT: ${params.RUN_LINT}"
                echo "   GENERATE_ALLURE: ${params.GENERATE_ALLURE}"
                sh 'python3 --version'
                sh 'pwd'
                sh 'ls -la'
                sh '''
                    echo "🔍 Проверка доступности Selenoid..."
                    if curl -s -o /dev/null -w "%{http_code}" ${EXECUTOR_URL}/status | grep -q "200"; then
                        echo "✅ Selenoid доступен"
                        echo "📊 Доступные браузеры:"
                        curl -s ${EXECUTOR_URL}/status | python3 -m json.tool || echo "Не удалось получить список браузеров"
                    else
                        echo "⚠️ Selenoid не доступен по адресу ${EXECUTOR_URL}"
                        echo "Проверьте, запущен ли контейнер selenoid"
                    fi
                '''
            }
        }

        stage('Setup') {
            steps {
                echo '📦 Установка зависимостей...'
                sh '''
                    python3 -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest-html pytest-xdist
                '''
            }
        }

        stage('Lint') {
            when {
                expression { params.RUN_LINT == true }
            }
            steps {
                echo '🔍 Проверка качества кода...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    flake8 src/ tests/ --max-line-length=100 --statistics || true
                '''
            }
        }

        stage('Test') {
            steps {
                echo '🚀 Запуск тестов на Selenoid...'
                sh '''
                    rm -rf allure-results reports
                    mkdir -p allure-results reports
                    . ${VENV_PATH}/bin/activate

                    if [ ! -d "tests" ] || [ -z "$(ls -A tests 2>/dev/null)" ]; then
                        echo "❌ Ошибка: Директория tests пуста или не существует!"
                        echo "Пожалуйста, добавьте тесты в директорию tests/"
                        exit 1
                    fi

                    echo "🔧 Запуск тестов с параметрами:"
                    echo "   Браузер: ${BROWSER}"
                    echo "   Версия: ${BROWSER_VERSION}"
                    echo "   Executor: ${EXECUTOR_URL}"

                    pytest tests/ \
                        --junitxml=reports/junit.xml \
                        --html=reports/report.html \
                        --self-contained-html \
                        --browser=${BROWSER} \
                        --browser-version=${BROWSER_VERSION} \
                        --executor=selenoid \
                        --selenoid-url=${EXECUTOR_URL} \
                        ${PYTEST_ARGS}
                '''
            }
        }

        stage('Generate Allure Report') {
            when {
                expression { params.GENERATE_ALLURE == true }
            }
            steps {
                echo '📊 Генерация Allure отчета...'
                script {
                    // Проверяем наличие Allure в системе
                    def allureInstalled = sh(script: 'command -v allure', returnStatus: true) == 0

                    if (allureInstalled && fileExists('allure-results')) {
                        sh '''
                            mkdir -p allure-report
                            allure generate allure-results -o allure-report --clean
                            echo "✅ Allure отчет сгенерирован"
                        '''
                    } else if (!allureInstalled) {
                        echo "⚠️ Allure не установлен. Пропускаем генерацию отчета."
                        echo "💡 Для установки Allure выполните: sudo apt-get install allure"
                    } else {
                        echo "⚠️ Нет результатов Allure для генерации отчета"
                    }
                }
            }
        }
    }

    post {
        always {
            echo '📈 Публикация отчетов...'

            // Публикация JUnit отчетов
            script {
                if (fileExists('reports/junit.xml')) {
                    junit allowEmptyResults: true, testResults: 'reports/junit.xml'
                    echo '✅ JUnit отчет опубликован'
                } else {
                    echo '⚠️ JUnit отчет не найден'
                }
            }

            // Сохраняем артефакты
            archiveArtifacts artifacts: 'allure-results/*, reports/*', allowEmptyArchive: true
        }

        success {
            echo "✅ Сборка успешна! Все тесты пройдены."
        }

        failure {
            echo "❌ Сборка провалена! Некоторые тесты не прошли."
            echo "Проверьте:"
            echo "  1. Доступен ли Selenoid: ${EXECUTOR_URL}"
            echo "  2. Доступен ли PrestaShop: ${PRESTASHOP_URL}"
            echo "  3. Правильные ли версии браузеров указаны"
        }

        cleanup {
            echo '🧹 Очистка workspace...'
            cleanWs()
        }
    }
}
