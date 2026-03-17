# AWS Compute Evolution

One application, five deployment models — demonstrating the AWS compute spectrum from EC2 to EKS.

Each directory deploys the same Python URL checker using a progressively more abstracted compute service, highlighting the tradeoffs in complexity, scalability, and operational overhead.

## The Application

A Python URL availability checker that takes a list of endpoints, checks their HTTP status, and reports which are healthy. ~50 lines, zero external dependencies — intentionally simple so the focus stays on **how** it's deployed, not **what** it does.

```
  ✓ [200] https://aws.amazon.com
  ✓ [200] https://docs.python.org
  ✓ [200] https://httpstat.us/200
  ✗ [503] https://httpstat.us/503

3/4 healthy
```

## Deployment Models

| # | Model | Directory | What Changes |
|---|---|---|---|
| 1 | **EC2** | [`ec2/`](ec2/) | App runs on a virtual machine, accessed via Session Manager |
| 2 | **Lambda** | [`lambda/`](lambda/) | App becomes a serverless function — no server to manage |
| 3 | **Docker + ECR** | [`docker/`](docker/) | App is containerized and pushed to a private registry |
| 4 | **ECS Fargate** | [`ecs-fargate/`](ecs-fargate/) | Container runs as a managed task — no host to manage |
| 5 | **EKS** | [`eks/`](eks/) | Container runs in Kubernetes with declarative manifests |

## Quick Comparison

| | EC2 | Lambda | Fargate | EKS |
|---|---|---|---|---|
| Scaling | Manual/ASG | Automatic | Service auto-scale | HPA |
| Cold start | None | ~200ms | ~30s | ~10s |
| Ops overhead | High | None | Low | High |
| Cost (idle) | ~$8/mo | $0 | $0 | ~$73/mo |

See [`COMPARISON.md`](COMPARISON.md) for the full decision matrix with cost analysis and use-case guidance.

## Project Structure

```
├── app/                  # Shared application code
│   └── url_checker.py
├── ec2/                  # EC2 user data deployment
├── lambda/               # Lambda function deployment
├── docker/               # Dockerfile + ECR push
├── ecs-fargate/          # Fargate task definition
├── eks/                  # Kubernetes manifests
└── COMPARISON.md         # Full tradeoff analysis
```

## Key Takeaway

There is no "best" compute service — only the right one for the workload. This project demonstrates that choosing between EC2, Lambda, Fargate, and EKS is an engineering decision driven by scaling requirements, operational capacity, cost constraints, and team expertise.

## Author

Emmanuel Fornah
