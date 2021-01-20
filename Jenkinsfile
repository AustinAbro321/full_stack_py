pipeline {
    agent any

    stages {
        stage('stop'){
            steps{
                sh 'docker stop container_fsp'
            }
        }

        stage('build') {
            steps {
                sh 'docker build . -t full_stack_py'
                sh 'docker run -d -p 8000:8000 full_stack_py -t container_fsp'       

            }
        }
    }
}
