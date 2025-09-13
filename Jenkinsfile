pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'mani789'
        DOCKER_HUB_REPO = 'mlops-house-price'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/manikanta63043/mlops-house-price.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_USER}/${DOCKER_HUB_REPO}:latest")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_USER}") {
                            docker.image("${DOCKER_HUB_USER}/${DOCKER_HUB_REPO}:latest").push()
                        }
                    }
                }
            }
        }
    }
}
