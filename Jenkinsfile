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
        booleanParam(
            name: 'HEADLESS',
            defaultValue: true,
            description: 'Запускать браузер в headless режиме?'
        )
    }

    environment {
        VENV_PATH = "${WORKSPACE}/.venv"
        EXECUTOR_URL = "${params.EXECUTOR_URL}"
        PRESTASHOP_URL = "${params.PRESTASHOP_URL}"
        BROWSER = "${params.BROWSER}"
        BROWSER_VERSION = "${params.BROWSER_VERSION}"
        FLOW_COUNT = "${params.FLOW_COUNT}"
        HEADLESS = "${params.HEADLESS}"
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
                echo "   HEADLESS: ${params.HEADLESS}"
                echo "   PYTEST_ARGS: ${params.PYTEST_ARGS}"
                echo "   RUN_LINT: ${params.RUN_LINT}"
                echo "   GENERATE_ALLURE: ${params.GENERATE_ALLURE}"
                sh 'python3 --version'
                sh 'pwd'
                sh 'ls -la'
                // Проверяем наличие браузеров для локального запуска
                sh '''
                    echo "🔍 Проверка браузеров для локального запуска:"
                    if command -v google-chrome &> /dev/null || command -v google-chrome-stable &> /dev/null; then
                        echo "✅ Chrome установлен"
                    else
                        echo "⚠️ Chrome не найден - тесты могут не запуститься локально"
                    fi
                    if command -v firefox &> /dev/null; then
                        echo "✅ Firefox установлен"
                    else
                        echo "⚠️ Firefox не найден"
                    fi
                    if command -v chromedriver &> /dev/null; then
                        echo "✅ ChromeDriver установлен"
                    else
                        echo "⚠️ ChromeDriver не найден"
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
                echo '🚀 Запуск тестов локально...'
                sh '''
                    rm -rf allure-results reports
                    mkdir -p allure-results reports
                    . ${VENV_PATH}/bin/activate

                    if [ ! -d "tests" ] || [ -z "$(ls -A tests 2>/dev/null)" ]; then
                        echo "❌ Ошибка: Директория tests пуста или не существует!"
                        exit 1
                    fi

                    # Запускаем тесты локально
                    echo "🔧 Запуск в режиме: ${HEADLESS}"
                    if [ "${HEADLESS}" = "true" ]; then
                        echo "🖥️ Headless режим"
                        HEADLESS_ARG="--headless"
                    else
                        echo "🖥️ Обычный режим"
                        HEADLESS_ARG=""
                    fi

                    # Пытаемся запустить с xvfb-run если доступен
                    if command -v xvfb-run &> /dev/null; then
                        echo "🔄 Использую xvfb-run"
                        xvfb-run -a pytest tests/ \
                            --junitxml=reports/junit.xml \
                            --html=reports/report.html \
                            --self-contained-html \
                            --browser=${BROWSER} \
                            --executor=local \
                            ${HEADLESS_ARG} \
                            ${PYTEST_ARGS}
                    else
                        echo "⚠️ xvfb-run не найден, запускаю напрямую"
                        pytest tests/ \
                            --junitxml=reports/junit.xml \
                            --html=reports/report.html \
                            --self-contained-html \
                            --browser=${BROWSER} \
                            --executor=local \
                            ${HEADLESS_ARG} \
                            ${PYTEST_ARGS}
                    fi
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
                    def allureInstalled = sh(script: 'command -v allure', returnStatus: true) == 0

                    if (allureInstalled && fileExists('allure-results')) {
                        sh '''
                            mkdir -p allure-report
                            allure generate allure-results -o allure-report --clean
                            echo "✅ Allure отчет сгенерирован"
                        '''
                    } else {
                        echo "⚠️ Allure не установлен или нет результатов. Пропускаем."
                    }
                }
            }
        }
    }

    post {
        always {
            echo '📈 Публикация отчетов...'

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
        }
    }
}
