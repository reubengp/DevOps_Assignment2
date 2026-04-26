# Deployment Strategies

## 1. Rolling Update
- This is the deployment method used in this project.
- Kubernetes replaces old pods with new pods gradually.
- This gives simple updates with low downtime.
- In this project, the deployment uses `strategy: type: RollingUpdate`.
- The old version is not removed all at once.
- Kubernetes starts a new pod first, checks that it is running correctly, and then removes an old pod.
- This process continues until all old pods are replaced by new pods.
- Because the pods are updated one by one, the application stays available during deployment.
- If the new version has a problem, rollback can be done using:

```bash
kubectl rollout undo deployment/aceest-fitness-deployment
```

Used file:
- `k8s/deployment.yaml`

## 2. Blue-Green Deployment
- Mentioned for reference only.

## 3. Canary Deployment
- Mentioned for reference only.

## 4. Shadow Deployment
- Mentioned for reference only.

## 5. A/B Testing
- Mentioned for reference only.
