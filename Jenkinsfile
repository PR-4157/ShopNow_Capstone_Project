pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'chmod +x scripts/build.sh'
                sh './scripts/build.sh'
            }
        }

        stage('Run Trivy Scan') {
            steps {
                sh 'chmod +x scripts/scan.sh'
                sh './scripts/scan.sh'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*.json', fingerprint: true
            }
        }

    }

    post {
        always {
            echo 'Pipeline Finished'
        }

        success {
            echo 'Security Scan Passed'
        }

        failure {
            echo 'Security Scan Failed'
        }
    }
}