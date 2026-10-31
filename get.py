import sys
import json
import requests
from datetime import datetime, timezone

username = sys.argv[1]
filename = sys.argv[2]

url = f"https://www.credly.com/users/{username}/badges.json"

r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
r.raise_for_status()

entry = {
    "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    "username": username,
    "data": r.json()
}

with open(filename, "a") as f:
    f.write(json.dumps(entry) + "\n")
