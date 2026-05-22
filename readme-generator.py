import sys
import xml.etree.ElementTree as ET
import requests

FEED_URL = "https://rss.nytimes.com/services/xml/rss/nyt/recent.xml"

r = requests.get(FEED_URL, timeout=15)
r.raise_for_status()
root = ET.fromstring(r.content)

items = root.findall(".//item")
if not items:
    sys.exit(f"no <item> elements in feed (got {len(r.content)} bytes)")

for item in items:
    link = (item.findtext("link") or "").strip()
    if "cooking.nytimes.com" in link:
        continue
    title = (item.findtext("title") or "").strip()
    description = (item.findtext("description") or "(No description)").strip()
    print(f"**{title}**\\")
    print(f"`{description}`\\")
    print(f"{link}\n")
