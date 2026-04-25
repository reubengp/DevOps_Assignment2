# ACEest Fitness & Gym CI/CD Project

This is a simple Flask-based DevOps project for a college-level CI/CD assignment. It includes a Flask app, pytest, Docker, Jenkins, SonarQube, and Kubernetes files for local deployment.

## 1. Project Folder Structure

```text
ACEest-Fitness-Gym/
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
|-- app.py
|-- Dockerfile
|-- Jenkinsfile
|-- README.md
|-- report.md
|-- requirements.txt
`-- sonar-project.properties
```

## 2. Minimal Setup

Install these tools first:

- Python 3.11+
- Git
- Docker Desktop
- Java 17 or Java 21 for Jenkins
- Jenkins
- SonarQube
- Minikube
- kubectl

## 3. Flask Application Setup

Create virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

- `http://127.0.0.1:5001/`
- `http://127.0.0.1:5001/workouts`
- `http://127.0.0.1:5001/members`
- `http://127.0.0.1:5001/plans`

## 4. Run Unit Tests

```bash
pytest tests -v
```

## 5. Docker Commands

Build image:

```bash
docker build -t aceest-fitness-gym .
```

Run container:

```bash
docker run -d -p 5001:5001 --name aceest-app aceest-fitness-gym
```

Check in browser:

```text
http://localhost:5001/
```

## 6. Jenkins Pipeline Steps

The Jenkins pipeline does:

1. Checkout code from GitHub
2. Install Python dependencies
3. Run pytest
4. Run SonarQube scan
5. Build Docker image
6. Push Docker image to Docker Hub

Before running Jenkins pipeline:

- Install Docker in the Jenkins machine
- Install SonarQube Scanner plugin
- Add Docker Hub credentials in Jenkins as `dockerhub-creds`
- Add SonarQube server in Jenkins as `sonarqube-server`
- Replace the Docker image name only if you want something different from `reuben001/aceest-fitness-gym`

## 7. SonarQube Setup

1. Start SonarQube locally.
2. Create a project in SonarQube.
3. Keep the project key same as in `sonar-project.properties`.
4. In Jenkins, configure SonarQube server name as `sonarqube-server`.
5. Run the Jenkins pipeline.

## 8. Kubernetes Local Deployment

Start minikube:

```bash
minikube start
```

Apply files:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check resources:

```bash
kubectl get pods
kubectl get services
```

Open service:

```bash
minikube service aceest-fitness-service
```

## 9. GitHub Version Control Strategy

Suggested branches:

- `main` for stable code
- `dev` for integration
- `feature/flask-app`
- `feature/tests`
- `feature/docker-setup`
- `feature/jenkins-pipeline`
- `feature/k8s-deployment`

Suggested commit style:

- `feat: add modular Flask routes`
- `test: add pytest cases for all endpoints`
- `build: add Dockerfile for Flask app`
- `ci: add Jenkins pipeline stages`
- `docs: add project report and setup guide`

Suggested tags:

- `v1.0.0` for first complete version
- `v1.1.0` after improvements

## 10. CI/CD Flow

```text
GitHub -> Jenkins -> Pytest -> SonarQube -> Docker Build -> Docker Hub -> Kubernetes Rolling Update Deployment
```

Simple flow:

- Developer pushes code to GitHub
- Jenkins pulls latest code
- Jenkins installs dependencies
- Jenkins runs tests
- Jenkins checks code quality with SonarQube
- Jenkins builds Docker image
- Jenkins pushes image to Docker Hub
- Kubernetes pulls image and runs app

## 11. Common Errors and Fixes

### Port already in use

Error:

```text
Address already in use
```

Fix:

- Stop old app/container using the port
- Or run another port like `docker run -p 5002:5001 ...`

### Docker image not found

Fix:

- Check image name carefully
- Build image again
- Make sure Docker Desktop is running

### Jenkins pipeline fails at Docker push

Fix:

- Check Docker Hub username
- Check Jenkins credentials id
- Run `docker login` once manually for testing

### Kubernetes image pull error

Fix:

- Push image to Docker Hub first
- Make sure image name in deployment file is correct
- Use public image or configure secret for private image

### SonarQube scan fails

Fix:

- Make sure SonarQube server is running
- Check project key
- Check scanner setup in Jenkins

## 12. Important Note

This project is made simple on purpose so it is easy to understand, run, and submit.
