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
            defaultValue: 'http://localhost:8080/',
            description: 'URL адрес PrestaShop (например: http://localhost:8080/)'
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
                    # Устанавливаем pytest-html если его нет в requirements
                    pip install pytest-html pytest-xdist || true
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
                echo '🚀 Запуск тестов...'
                sh '''
                    rm -rf allure-results reports
                    mkdir -p allure-results reports
                    . ${VENV_PATH}/bin/activate

                    # Проверяем наличие тестов
                    if [ ! -d "tests" ] || [ -z "$(ls -A tests 2>/dev/null)" ]; then
                        echo "❌ Ошибка: Директория tests пуста или не существует!"
                        echo "Пожалуйста, добавьте тесты в директорию tests/"
                        exit 1
                    fi

                    # Запускаем тесты с передачей параметров
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
                    def allureInstalled = sh(script: 'command -v allure', returnStatus: true) == 0

                    if (allureInstalled && fileExists('allure-results') && fileExists('allure-results/*.json')) {
                        sh '''
                            mkdir -p allure-report
                            allure generate allure-results -o allure-report --clean
                            echo "✅ Allure отчет сгенерирован"
                        '''
                    } else if (!allureInstalled) {
                        echo "⚠️ Allure не установлен. Пропускаем генерацию отчета."
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

            script {
                if (fileExists('reports/junit.xml')) {
                    junit allowEmptyResults: true, testResults: 'reports/junit.xml'
                    echo '✅ JUnit отчет опубликован'
                } else {
                    echo '⚠️ JUnit отчет не найден'
                }
            }

            script {
                try {
                    if (fileExists('reports/report.html')) {
                        publishHTML target: [
                            allowMissing: true,
                            alwaysLinkToLastBuild: true,
                            keepAll: true,
                            reportDir: 'reports',
                            reportFiles: 'report.html',
                            reportName: 'Pytest HTML Report'
                        ]
                        echo '✅ Pytest HTML отчет опубликован'
                    }
                } catch (Exception e) {
                    echo "⚠️ Плагин HTML Publisher не установлен: ${e.message}"
                }
            }

            script {
                if (params.GENERATE_ALLURE == true && fileExists('allure-report/index.html')) {
                    try {
                        publishHTML target: [
                            allowMissing: true,
                            alwaysLinkToLastBuild: true,
                            keepAll: true,
                            reportDir: 'allure-report',
                            reportFiles: 'index.html',
                            reportName: 'Allure Report'
                        ]
                        echo '✅ Allure отчет опубликован'
                    } catch (Exception e) {
                        echo "⚠️ Не удалось опубликовать Allure отчет"
                    }
                }
            }

            archiveArtifacts artifacts: 'allure-results/*, reports/*', allowEmptyArchive: true
        }

        success {
            echo "✅ Сборка успешна! Все тесты пройдены."
        }

        failure {
            echo "❌ Сборка провалена! Некоторые тесты не прошли или тесты отсутствуют."
        }

        cleanup {
            echo '🧹 Очистка workspace...'
            cleanWs()
        }
    }
}
