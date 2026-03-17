# EKS Deployment

Deploy the URL checker to a managed Kubernetes cluster with declarative manifests.

## Deploy

```bash
# Connect to cluster
aws eks update-kubeconfig --name url-checker-cluster --region us-east-1

# Apply manifest
kubectl apply -f deployment.yaml

# Verify
kubectl get pods -l app=url-checker
kubectl logs -l app=url-checker
```

## Scale

```bash
kubectl scale deployment url-checker --replicas=4
```

## Teardown

```bash
kubectl delete -f deployment.yaml
```

## Characteristics

| Attribute | Value |
|---|---|
| Scaling | Horizontal Pod Autoscaler (HPA) |
| Cold start | ~10s (pod scheduling + pull) |
| Ops overhead | High — cluster management, RBAC, networking |
| Cost model | Control plane ($0.10/hr) + worker nodes |
| Best for | Multi-service architectures, complex orchestration |
