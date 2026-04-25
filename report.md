# ACEest Fitness & Gym CI/CD Project Report

## Introduction

This project is a simple Flask-based fitness application created for a DevOps and CI/CD assignment. The main goal of the project is to show how a basic web application can move from code development to testing, containerization, continuous integration, and deployment on Kubernetes.

The application is called **ACEest Fitness & Gym**. It provides four simple API endpoints:

- `/` for the home route
- `/workouts` for workout details
- `/members` for gym member details
- `/plans` for membership plans

The application is intentionally kept simple so that the main focus stays on the CI/CD pipeline and deployment process.

## Project Objectives

The main objectives of this project were:

1. Build a simple Flask application with clean structure.
2. Add unit testing using Pytest.
3. Containerize the application using Docker.
4. Create a Jenkins pipeline for continuous integration and delivery.
5. Add SonarQube for basic code quality checking.
6. Deploy the application locally using Kubernetes and Minikube.
7. Understand common deployment strategies used in DevOps.

## Tools Used

The following tools were used in this project:

- **Flask** for the web application
- **Pytest** for unit testing
- **GitHub** for source code management
- **Docker** for containerization
- **Jenkins** for CI/CD pipeline automation
- **SonarQube** for code quality scanning
- **Kubernetes** with **Minikube** for local deployment

## Application Development

The Flask application was developed in a modular format. Instead of writing all logic in a single file, the project uses a small `app` package.

- `app/__init__.py` creates the Flask app
- `app/routes.py` contains route definitions
- `app/data.py` stores simple sample data
- `app.py` is the main runner file

This structure makes the project cleaner and easier to maintain. The routes return JSON responses so the app is easy to test and use in Docker or Kubernetes.

## Testing with Pytest

Pytest was used to test all four endpoints. The tests check:

- response status code
- expected JSON keys
- sample values from returned data

Testing is an important part of CI because Jenkins can automatically run tests every time code is pushed to GitHub. If any test fails, the pipeline can stop before deployment.

The command used is:

```bash
pytest tests -v
```

## Docker Implementation

The application was containerized using Docker. A simple `Dockerfile` was written using `python:3.11-slim` as the base image.

The Docker process follows these steps:

1. Set working directory
2. Copy `requirements.txt`
3. Install dependencies
4. Copy application files
5. Expose port 5001
6. Run the Flask app

This makes the application portable and easy to run on any machine with Docker.

Build command:

```bash
docker build -t aceest-fitness-gym .
```

Run command:

```bash
docker run -d -p 5001:5001 aceest-fitness-gym
```

## Jenkins CI/CD Pipeline

The Jenkins pipeline was defined in the `Jenkinsfile`. The pipeline contains the following stages:

1. Checkout
2. Install Dependencies
3. Run Tests
4. SonarQube Scan
5. Build Docker Image
6. Push to Docker Hub

This means whenever code is pushed to GitHub, Jenkins can automatically take the latest version, test it, build a Docker image, and push it to Docker Hub. This saves manual effort and reduces deployment mistakes.

Some Jenkins setup is required before running the pipeline:

- Docker must be installed on the Jenkins system
- Docker Hub credentials must be added
- SonarQube plugin and scanner must be configured

## SonarQube Integration

SonarQube was added to perform basic static code analysis. It helps in checking code quality, maintainability, and possible issues. A minimal `sonar-project.properties` file was added for configuration.

In this project, SonarQube is kept simple because the project is small. The main purpose is to show integration with Jenkins and demonstrate a complete CI pipeline.

## Kubernetes Deployment

Kubernetes files were added inside the `k8s` folder:

- `deployment.yaml`
- `service.yaml`

The Kubernetes setup uses a Rolling Update deployment. A single deployment file is used, and Kubernetes updates pods gradually when a new version of the image is applied. This method is simple, practical, and easy to manage in a local Minikube environment.

Main Kubernetes commands:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service aceest-fitness-service
```

This setup is enough for a local demo deployment.

## Deployment Strategies

Different deployment strategies were also studied in this project:

- **Rolling Update**: gradually replace old pods with new pods
- **Blue-Green**: maintain two environments and switch traffic after testing
- **Canary**: send small traffic to new version before full release
- **Shadow**: mirror traffic to new version without affecting users
- **A/B Testing**: split users between versions based on defined rules

For this assignment, Rolling Update is the main deployment method used in the Kubernetes files, and the other strategies are explained at a basic level in `k8s/strategies.md`.

## CI/CD Flow Explanation

The full pipeline flow is:

**GitHub -> Jenkins -> Docker -> Kubernetes**

Step by step:

1. Developer pushes code to GitHub.
2. Jenkins pulls the latest code.
3. Jenkins installs dependencies.
4. Jenkins runs Pytest.
5. Jenkins runs SonarQube scan.
6. Jenkins builds Docker image.
7. Jenkins pushes image to Docker Hub.
8. Kubernetes pulls the image and runs the application.

This flow shows how DevOps automation helps move code from development to deployment with less manual work.

## Challenges and Fixes

Some common issues that may happen are:

- Port conflict on port 5001
- Docker daemon not running
- Jenkins credentials not configured
- Docker image name mismatch in Kubernetes
- SonarQube server not started

These problems can be fixed by checking the service status, verifying credentials, and making sure the correct image name and port are used.

## Conclusion

This project successfully demonstrates a simple but complete CI/CD pipeline for a Flask application. Even though the app is small, it includes important DevOps concepts such as testing, code quality checking, Docker, Jenkins automation, and Kubernetes deployment.

The project is easy to understand and suitable for academic submission because it focuses on practical implementation rather than complex production architecture.
