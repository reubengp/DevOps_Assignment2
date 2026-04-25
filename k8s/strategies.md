# Deployment Strategies

## 1. Rolling Update
- This is the deployment method used in this project.
- Kubernetes replaces old pods with new pods gradually.
- This gives simple updates with low downtime.
- In this project, the deployment uses `strategy: type: RollingUpdate`.

Used file:
- `k8s/deployment.yaml`

## 2. Blue-Green Deployment
- Keep two versions: blue and green.
- One version handles live traffic, the other is the new version.
- After testing green, switch the service from blue to green.

## 3. Canary Deployment
- Send a small amount of traffic to the new version first.
- Example: run 1 pod of new version and 3 pods of old version.
- If stable, increase new version replicas.

## 4. Shadow Deployment
- New version receives a copy of real traffic, but users still see old version response.
- Used for testing performance and logs without affecting users.
- In local projects, this is mostly shown as a concept and architecture idea.

## 5. A/B Testing
- Users are split into different versions based on rule or header.
- Example: version A for normal users, version B for trial users.
- Usually handled by ingress, API gateway, or application logic.
