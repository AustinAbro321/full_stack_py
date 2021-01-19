pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'docker build .'
                sh 'docker-compose up -d --build'          
                sh 'python3 manage.py runserver 0.0.0.0:8000'      
            }
        }
    }
}
