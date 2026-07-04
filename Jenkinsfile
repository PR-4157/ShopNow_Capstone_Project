pipeline {
    agent any

    stages {

        stage('Build Docker Images') {
            steps {
                sh 'chmod +x scripts/build.sh'
                sh './scripts/build.sh'
            }
        }

        stage('Scan Docker Images') {
            steps {
                sh 'chmod +x scripts/scan.sh'
                sh './scripts/scan.sh'
            }
        }

    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.json', fingerprint: true
        }

        success {
            echo 'Security pipeline completed successfully!'
        }

        failure {
            echo 'Security pipeline failed!'
        }
    }
}