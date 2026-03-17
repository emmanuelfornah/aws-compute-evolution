# EC2 Deployment

Launch an EC2 instance with the URL checker installed via user data, accessed through Session Manager.

## Deploy

```bash
aws ec2 run-instances \
  --image-id ami-0c02fb55956c7d316 \
  --instance-type t3.micro \
  --iam-instance-profile Name=SSMInstanceProfile \
  --user-data file://user-data.sh \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=url-checker}]'
```

## Access

```bash
aws ssm start-session --target <instance-id>
python3 /opt/url-checker/url_checker.py
```

## Teardown

```bash
aws ec2 terminate-instances --instance-ids <instance-id>
```

## Characteristics

| Attribute | Value |
|---|---|
| Scaling | Manual / Auto Scaling Group |
| Cold start | None (always running) |
| Ops overhead | High — patching, monitoring, SSH keys |
| Cost model | Per-hour (running or idle) |
| Best for | Long-running, stateful workloads |
