pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python app.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python -m unittest discover'
            }
        }
        stage('Lint') {
            steps {
                echo 'Linting..'
                sh 'pylint app.py'
            }
        }
        stage('Report') {
            steps {
                echo 'Publishing reports..'
                junit '**/tests.xml'
                warnings canComputeNew: false, defaultEncoding: '', healthy: '', includePattern: '', unHealthy: ''
            }
        }
    }
}
