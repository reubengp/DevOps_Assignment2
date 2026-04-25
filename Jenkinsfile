pipeline {
    agent any

    environment {
        IMAGE_NAME = "reuben001/aceest-fitness-gym"
        IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKER_BIN = "/usr/local/bin/docker"
        PATH = "/usr/local/bin:/Applications/Docker.app/Contents/Resources/bin:/opt/homebrew/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest tests'
            }
        }

        stage('SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('sonarqube-server') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '$DOCKER_BIN build -t $IMAGE_NAME:$IMAGE_TAG -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | $DOCKER_BIN login -u $DOCKER_USER --password-stdin'
                    sh '$DOCKER_BIN push $IMAGE_NAME:$IMAGE_TAG'
                    sh '$DOCKER_BIN push $IMAGE_NAME:latest'
                }
            }
        }
    }
}
