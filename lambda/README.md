# Lambda Deployment

Deploy the URL checker as a serverless function — no infrastructure to manage.

## Deploy

```bash
cd ../app
zip url_checker.zip url_checker.py

aws lambda create-function \
  --function-name url-checker \
  --runtime python3.13 \
  --handler url_checker.lambda_handler \
  --zip-file fileb://url_checker.zip \
  --role arn:aws:iam::<ACCOUNT_ID>:role/LambdaBasicRole
```

## Invoke

```bash
aws lambda invoke --function-name url-checker output.json
cat output.json | python3 -m json.tool
```

## Teardown

```bash
aws lambda delete-function --function-name url-checker
```

## Characteristics

| Attribute | Value |
|---|---|
| Scaling | Automatic (concurrent executions) |
| Cold start | ~200ms (Python) |
| Ops overhead | None — fully managed |
| Cost model | Per-invocation + duration |
| Best for | Event-driven, bursty, short-lived tasks |
