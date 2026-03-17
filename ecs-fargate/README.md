# ECS Fargate Deployment

Run the URL checker as a serverless container on ECS Fargate — no EC2 instances to manage.

## Deploy

```bash
# Create CloudWatch log group
aws logs create-log-group --log-group-name /ecs/url-checker

# Register task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

# Create cluster
aws ecs create-cluster --cluster-name url-checker

# Run task
aws ecs run-task \
  --cluster url-checker \
  --task-definition url-checker \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[<SUBNET_ID>],securityGroups=[<SG_ID>],assignPublicIp=ENABLED}"
```

## View Logs

```bash
aws logs tail /ecs/url-checker --follow
```

## Teardown

```bash
aws ecs delete-cluster --cluster url-checker
aws logs delete-log-group --log-group-name /ecs/url-checker
```

## Characteristics

| Attribute | Value |
|---|---|
| Scaling | ECS Service auto scaling |
| Cold start | ~30s (task launch + image pull) |
| Ops overhead | Low — no host management |
| Cost model | Per-task vCPU-second + memory-second |
| Best for | Production containers without cluster management |
