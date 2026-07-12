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
        // Добавляем недостающие параметры
        booleanParam(
            name: 'RUN_LINT',
            defaultValue: false,
            description: 'Запускать ли линтер?'
        )
        booleanParam(
            name: 'GENERATE_COVERAGE',
            defaultValue: true,
            description: 'Генерировать ли отчет о покрытии?'
        )
    }

    environment {
        // WORKSPACE - автоматическая переменная Jenkins
        VENV_PATH = "${WORKSPACE}/.venv"
        // Можно также явно передать в переменные окружения для тестов
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
                sh 'python3 --version'
                sh 'pwd'
                sh 'echo "Workspace: ${WORKSPACE}"'
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
                echo 'Запуск тестов...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    mkdir -p reports allure-results
                    pytest tests/ \
                        --junitxml=reports/junit.xml \
                        --html=reports/report.html \
                        --cov=src \
                        --cov-report=xml:reports/coverage.xml \
                        --cov-report=html:reports/htmlcov \
                        ${PYTEST_ARGS}
                '''
            }
        }
    }

    post {
        always {
            echo '📈 Публикация отчетов...'
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'

            script {
                if (params.GENERATE_COVERAGE) {
                    publishHTML(target: [
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports/htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        success {
            echo "✅ Сборка успешна!"
        }
        failure {
            echo "❌ Сборка провалена!"
        }
        cleanup {
            echo '🧹 Очистка workspace...'
            cleanWs()
        }
    }
}
