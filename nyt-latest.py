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

print('<html><head><style>html,body,p,h4{margin:0;font-family:avenir;font-weight:normal;font-size:1em;line-height:1.4em}a{font-size:0.8em;}h4{font-size:1.6em;}body{margin-left:20px}</style></head><body>')

for item in items:
    link = (item.findtext("link") or "").strip()
    if "cooking.nytimes.com" in link:
        continue
    title = (item.findtext("title") or "").strip()
    print(f"<h4>{title}</h4>")
    print(f'<a href="{link}">{link}</a><br><br>')

print("</body></html>")
