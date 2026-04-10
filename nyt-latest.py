import os
import requests

API_KEY = os.environ.get("NYT_API_KEY", "")

url = "https://api.nytimes.com/svc/news/v3/content/all/all.json"
params = {"api-key": API_KEY}

r = requests.get(url, params=params)
data = r.json()

print('<html><head><style>html,body,p,h4{margin:0;font-family:avenir;font-weight:normal;font-size:1em;line-height:1.4em}a{font-size:0.8em;}h4{font-size:1.6em;}body{margin-left:20px}</style></head><body>')

for doc in data["results"]:
    if "cooking.nytimes.com" in doc["url"]:
        continue
    headline = doc["title"]
    web_url = doc["url"]
    print(f"<h4>{headline}</h4>")
    print(f'<a href="{web_url}">{web_url}</a><br><br>')

print("</body></html>")
