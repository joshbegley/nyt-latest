import sys
import requests
from datetime import datetime, timedelta
from pathlib import Path

def fetch(day):
    path = Path(f"{day:%Y-%m-%d}.pdf")
    if path.exists() and path.stat().st_size > 0:
        print(f"{day:%Y-%m-%d}: already have it")
        return
    url = f"https://static01.nyt.com/images/{day:%Y/%m/%d}/nytfrontpage/scan.pdf"
    r = requests.get(url)
    if r.status_code == 200:
        path.write_bytes(r.content)
        print(f"{day:%Y-%m-%d}: {len(r.content):,} bytes")
    else:
        print(f"{day:%Y-%m-%d}: HTTP {r.status_code}", file=sys.stderr)

args = sys.argv[1:]
start = datetime.strptime(args[0], '%Y-%m-%d') if args else datetime.now()
end = datetime.strptime(args[1], '%Y-%m-%d') if len(args) > 1 else start

while start <= end:
    fetch(start)
    start += timedelta(days=1)
