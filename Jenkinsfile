pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                docker-compose up -d
            }
        }
    }
}
