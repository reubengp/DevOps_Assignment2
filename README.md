# ACEfest Fitness & Gym CI/CD Project

## Introduction

This project was done for a DevOps CI/CD assignment. The application is a simple Flask-based fitness app called **ACEfest Fitness & Gym**. The main aim of the project is to show how a small application can go through testing, code quality check, Docker build, Jenkins pipeline, and Kubernetes deployment.

For submission alignment, the project includes `ACEest_Fitness.py` as the assignment-named Flask entry point and `VERSION_HISTORY.md` to summarize incremental versions of the same code base.

The app has the following routes:

- `/`
- `/workouts`
- `/members`
- `/plans`

## Project Structure

```text
ACEfest/
|-- app/
|   |-- __init__.py
|   |-- data.py
|   `-- routes.py
|-- k8s/
|   |-- deployment.yaml
|   |-- service.yaml
|   `-- strategies.md
|-- tests/
|   `-- test_routes.py
|-- .dockerignore
|-- .gitignore
|-- ACEest_Fitness.py
|-- VERSION_HISTORY.md
|-- app.py
|-- Dockerfile
|-- Jenkinsfile
|-- pytest.ini
|-- README.md
|-- report.md
|-- requirements.txt
`-- sonar-project.properties
```

## Tools Used

- Python
- Flask
- Pytest
- Git and GitHub
- Docker
- Jenkins
- SonarQube
- Kubernetes
- Minikube

## How to Run the Flask App

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Or run the assignment-named entry point:

```bash
python ACEest_Fitness.py
```

Open these in browser:

- `http://127.0.0.1:5001/`
- `http://127.0.0.1:5001/workouts`
- `http://127.0.0.1:5001/members`
- `http://127.0.0.1:5001/plans`

## How to Run Tests

```bash
pytest tests -v
```

This project has simple unit tests for all routes.

## Docker Setup

Build Docker image:

```bash
docker build -t reuben001/aceest-fitness-gym:latest .
```

Run Docker container:

```bash
docker run -d -p 5001:5001 --name aceest-app reuben001/aceest-fitness-gym:latest
```

Then open:

```text
http://localhost:5001/
```

## Jenkins Pipeline

The Jenkins pipeline file is in `Jenkinsfile`.

The pipeline stages are:

1. Checkout
2. Install Dependencies
3. Run Tests
4. SonarQube Scan
5. Build Docker Image
6. Push to Docker Hub

Important Jenkins setup used in this project:

- SonarQube server name: `sonarqube-server`
- Docker credentials ID: `dockerhub-creds`
- Sonar scanner tool name: `sonar-scanner`

## SonarQube

SonarQube is used in this project for static code analysis.

In this setup, SonarQube runs locally in Docker at:

```text
http://localhost:9000
```

The project key used is:

```text
aceest-fitness-gym
```

## Kubernetes Deployment

This project is deployed locally using Minikube.

Start Minikube:

```bash
minikube start
```

Apply Kubernetes files:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check pods and services:

```bash
kubectl get pods
kubectl get services
```

Open the service:

```bash
minikube service aceest-fitness-service
```

## Deployment Strategy Used

This project uses **Rolling Update**.

Rollback to the last stable version is supported through Kubernetes rollout history. If a deployment fails or the new version is unstable, the application can be reverted to the previous working release.

Reason:

- It is simple
- It is supported by Kubernetes by default
- It updates pods one by one
- It helps reduce downtime

How it works here:

- 2 replicas are used in deployment
- when a new version is applied, Kubernetes starts a new pod first
- after that, one old pod is removed
- this continues until all pods are updated

Rollback command:

```bash
kubectl rollout undo deployment/aceest-fitness-deployment
```

Useful rollback verification commands:

```bash
kubectl rollout status deployment/aceest-fitness-deployment
kubectl rollout history deployment/aceest-fitness-deployment
kubectl get pods
```

Other deployment methods like Blue-Green, Canary, Shadow, and A/B Testing are only mentioned for reference in this project.

## GitHub Version Control

This project is maintained using Git and GitHub.

Suggested branch names:

- `main`
- `feature/flask-app`
- `feature/tests`
- `feature/docker-setup`
- `feature/jenkins-pipeline`

Example commit messages:

- `feat: add Flask routes`
- `test: add route test cases`
- `build: add Dockerfile`
- `ci: add Jenkins pipeline`
- `docs: update README and report`

Example tag:

```text
v1.0.0
```

## CI/CD Flow

```text
GitHub -> Jenkins -> Pytest -> SonarQube -> Docker -> Docker Hub -> Kubernetes
```

Simple explanation:

- code is pushed to GitHub
- Jenkins pulls the latest code
- Jenkins installs dependencies
- Jenkins runs tests
- Jenkins runs SonarQube scan
- Jenkins builds Docker image
- Jenkins pushes image to Docker Hub
- Kubernetes pulls the image and runs the app

## Common Errors

### Port already in use

If port `5001` is busy:

- stop the old process
- or run Docker on another host port

Example:

```bash
docker run -d -p 5002:5001 --name aceest-app reuben001/aceest-fitness-gym:latest
```

### Docker push failed in Jenkins

Check:

- Docker Hub token
- Jenkins credential ID
- Docker username

### SonarQube not opening

Make sure SonarQube container is running:

```bash
docker start sonarqube
```

### Kubernetes image pull error

Check:

- image name is correct
- image is pushed to Docker Hub
- deployment file uses the correct image

## Final Note

This project was kept simple on purpose so it is easy to understand, run, and present for an academic assignment.
