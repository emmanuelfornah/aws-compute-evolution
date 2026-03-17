#!/bin/bash
set -euo pipefail

yum update -y
yum install -y python3

mkdir -p /opt/url-checker
cat > /opt/url-checker/url_checker.py << 'SCRIPT'
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
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {"url": url, "status": resp.status, "healthy": resp.status < 400}
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "healthy": False}
    except Exception as e:
        return {"url": url, "status": str(e), "healthy": False}

def check_all(urls=None):
    urls = urls or os.environ.get("CHECK_URLS", "").split(",") or DEFAULT_URLS
    urls = [u.strip() for u in urls if u.strip()]
    return [check_url(u) for u in urls]

if __name__ == "__main__":
    results = check_all()
    for r in results:
        icon = "✓" if r["healthy"] else "✗"
        print(f"  {icon} [{r['status']}] {r['url']}")
    healthy = sum(1 for r in results if r["healthy"])
    print(f"\n{healthy}/{len(results)} healthy")
SCRIPT

python3 /opt/url-checker/url_checker.py
