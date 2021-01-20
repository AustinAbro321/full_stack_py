pipeline {
    agent any

    stages {
        stage('stop'){
            steps{
                // sh 'docker rm -f syallbus_app && echo "container removed" || echo "container does not exist"'
                sh 'docker-compose stop && echo "container removed" || echo "container does not exist"'
            }
        }

        stage('build') {
            steps {
                sh 'docker build . -t full_stack_py'
                // sh 'docker run -d -p 8000:8000 --name syallbus_app full_stack_py'
                sh 'docker-compose up -d'
            }
        }
    }
}
