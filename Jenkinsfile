pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'docker build . -t full_stack_py'
                sh 'docker-compose up -d --build'       
                sh 'python --version'
                sh 'pip freeze'   
                sh 'python manage.py runserver 0.0.0.0:8000'      
            }
        }
    }
}
