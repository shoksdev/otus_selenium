pipeline {
    agent any

    parameters {
        string(
            name: 'EXECUTOR_URL',
            defaultValue: 'http://selenoid:4444/wd/hub',
            description: 'URL адрес Executor'
        )
        string(
            name: 'PRESTASHOP_URL',
            defaultValue: 'http://prestashop:80/',
            description: 'URL адрес PrestaShop'
        )
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox'],
            description: 'Выберите браузер'
        )
        choice(
            name: 'BROWSER_VERSION',
            choices: ['125.0', '127.0'],
            description: 'Версия браузера'
        )
        string(
            name: 'FLOW_COUNT',
            defaultValue: '4',
            description: 'Количество потоков'
        )
        text(
            name: 'PYTEST_ARGS',
            defaultValue: '--alluredir allure-results --strict-markers --tb=short --verbose',
            description: 'Аргументы для pytest'
        )
        booleanParam(
            name: 'RUN_LINT',
            defaultValue: false,
            description: 'Запускать линтер?'
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
                sh 'python3 --version'
                sh 'pwd'
                sh 'ls -la'
                sh '''
                    echo "🔍 Проверка доступности Selenoid..."
                    curl -s ${EXECUTOR_URL}/status || echo "⚠️ Selenoid не доступен"
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
                echo '🚀 Запуск тестов...'
                sh '''
                    rm -rf allure-results reports
                    mkdir -p allure-results reports
                    . ${VENV_PATH}/bin/activate

                    if [ ! -d "tests" ] || [ -z "$(ls -A tests 2>/dev/null)" ]; then
                        echo "❌ Ошибка: Директория tests пуста!"
                        exit 1
                    fi

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
    }

    post {
        always {
            echo '📈 Публикация отчетов...'
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
            archiveArtifacts artifacts: 'reports/*, allure-results/*', allowEmptyArchive: true
        }
        success {
            echo "✅ Сборка успешна!"
        }
        failure {
            echo "❌ Сборка провалена!"
        }
    }
}
