pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'docker build . -t full_stack_py'
                sh 'docker run -d -p 8000:8000 full_stack_py'       
                
            }
        }
    }
}
