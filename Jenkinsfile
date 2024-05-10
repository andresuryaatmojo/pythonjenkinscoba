pipeline {
    agent any

    tools {
        // Memastikan python dan pytest tersedia
        python 'Python3'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Kode build tidak spesifik, hanya pastikan skrip dapat dieksekusi
                sh 'python3 ops.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 -m pytest'
            }
        }
        stage('Lint') {
            steps {
                echo 'Linting the code...'
                // Contoh menggunakan pylint, tambahkan ini jika pylint ingin digunakan
                sh 'pylint *.py'
            }
        }
        stage('Report') {
            steps {
                echo 'Generating reports...'
                // Simulasikan generasi laporan, sesuaikan berdasarkan tools yang digunakan
                sh 'echo "Reports generated"'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
