# Docker + ECR Deployment

Containerize the URL checker and push to a private ECR registry.

## Build

```bash
docker build -t url-checker -f Dockerfile ../app/
docker run url-checker
```

## Push to ECR

```bash
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=us-east-1
REPO=${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/url-checker

aws ecr create-repository --repository-name url-checker
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $REPO

docker tag url-checker:latest ${REPO}:latest
docker push ${REPO}:latest
```

## Teardown

```bash
aws ecr delete-repository --repository-name url-checker --force
```

## Characteristics

| Attribute | Value |
|---|---|
| Scaling | Manual (run more containers) |
| Cold start | None (image cached) |
| Ops overhead | Medium — build pipeline, image management |
| Cost model | Per-hour (host machine) |
| Best for | Dev/CI parity, portable deployments |
