pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'docker build . -t full_stack_py'
                sh 'docker-compose up -d'       
            }
        }
    }
}
