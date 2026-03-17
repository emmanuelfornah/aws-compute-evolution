# Compute Model Comparison

## Decision Matrix

| | EC2 | Lambda | Docker/ECR | ECS Fargate | EKS |
|---|---|---|---|---|---|
| **Scaling** | Manual / ASG | Automatic | Manual | Service auto-scale | HPA |
| **Cold start** | None | ~200ms | None | ~30s | ~10s |
| **Ops overhead** | High | None | Medium | Low | High |
| **Cost model** | Per-hour | Per-invocation | Per-hour (host) | Per-task-second | Control plane + nodes |
| **Min cost** | ~$8/mo (t3.micro) | $0 (free tier) | Host-dependent | ~$0.01/run | ~$73/mo (control plane) |
| **Deployment** | User data / SSM | ZIP upload | docker push | Task definition | kubectl apply |
| **Portability** | AWS-only | AWS-only | Any Docker host | AWS-only | Any K8s cluster |
| **State** | Persistent (EBS) | Stateless | Ephemeral | Ephemeral | Persistent (PV) |

## When to Use What

### EC2
- Long-running processes that need persistent local state
- Applications requiring specific OS configurations or GPU access
- Workloads with steady, predictable traffic

### Lambda
- Event-driven processing (S3 triggers, API calls, schedules)
- Bursty workloads with idle periods
- Functions under 15 minutes execution time

### Docker + ECR
- Development and CI/CD environments needing production parity
- Building container images for downstream deployment (Fargate, EKS)
- Local testing before cloud deployment

### ECS Fargate
- Production container workloads without cluster management overhead
- Teams that want containers but not Kubernetes complexity
- Microservices with predictable scaling patterns

### EKS
- Multi-service architectures requiring service mesh, RBAC, custom operators
- Organizations already invested in Kubernetes tooling
- Workloads needing portability across cloud providers

## Cost Comparison (Running 24/7 for 1 Month)

```
EC2 (t3.micro):     ~$8/mo
Lambda (1M calls):  ~$0.20/mo
ECS Fargate (1 task): ~$15/mo
EKS (1 node):       ~$80/mo (control plane + t3.medium)
```

## Complexity Progression

```
Lambda          ████░░░░░░  Simplest — zero infrastructure
EC2             █████░░░░░  Familiar — traditional server model
Docker/ECR      ██████░░░░  Packaging — adds build pipeline
ECS Fargate     ███████░░░  Orchestration — adds task management
EKS             ██████████  Full platform — adds K8s complexity
```
