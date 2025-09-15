pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/manikanta63043/mlops-house-price.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t mlops-house-price:latest .'
                }
            }
        }

        stage('Tag & Push Docker Image') {
            steps {
                script {
                    sh 'docker tag mlops-house-price:latest mani789/mlops-house-price:latest'
                    sh 'docker login -u mani789 -p YOUR_DOCKER_HUB_PASSWORD'
                    sh 'docker push mani789/mlops-house-price:latest'
                }
            }
        }
    }
}

