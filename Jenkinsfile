pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKERHUB_REPO = "mani789/mlops-house-price"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/manikanta63043/mlops-house-price.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t mlops-house-price:latest .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                script {
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        }

        stage('Tag & Push Docker Image') {
            steps {
                script {
                    sh "docker tag mlops-house-price:latest $DOCKERHUB_REPO:latest"
                    sh "docker push $DOCKERHUB_REPO:latest"
                }
            }
        }
    }
}

