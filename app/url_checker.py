"""URL availability checker — checks HTTP status of configured endpoints."""

import json
import os
import urllib.request
import urllib.error

DEFAULT_URLS = [
    "https://aws.amazon.com",
    "https://docs.python.org",
    "https://httpstat.us/200",
    "https://httpstat.us/503",
]


def check_url(url, timeout=5):
    "Check a single URL and return status."
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {"url": url, "status": resp.status, "healthy": resp.status < 400}
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "healthy": False}
    except Exception as e:
        return {"url": url, "status": str(e), "healthy": False}


def check_all(urls=None):
    "Check all URLs and return results."
    urls = urls or os.environ.get("CHECK_URLS", "").split(",") or DEFAULT_URLS
    urls = [u.strip() for u in urls if u.strip()]
    return [check_url(u) for u in urls]


def lambda_handler(event, context):
    "AWS Lambda entry point."
    results = check_all()
    healthy = sum(1 for r in results if r["healthy"])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "summary": f"{healthy}/{len(results)} healthy",
            "results": results,
        }),
    }


if __name__ == "__main__":
    results = check_all()
    for r in results:
        icon = "✓" if r["healthy"] else "✗"
        print(f"  {icon} [{r['status']}] {r['url']}")
    healthy = sum(1 for r in results if r["healthy"])
    print(f"\n{healthy}/{len(results)} healthy")
