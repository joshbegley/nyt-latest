import os
import requests

API_KEY = os.environ.get("NYT_API_KEY", "")

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {"sort": "newest", "api-key": API_KEY}

r = requests.get(url, params=params)
data = r.json()

print('<html><head><style>html,body,p,h4{margin:0;font-family:avenir;font-weight:normal;font-size:1em;line-height:1.4em}a{font-size:0.8em;}h4{font-size:1.6em;}body{margin-left:20px}</style></head><body>')

for doc in data["response"]["docs"]:
    if "cooking.nytimes.com" in doc["web_url"]:
        continue
    headline = doc["headline"]["main"]
    web_url = doc["web_url"]
    print(f"<h4>{headline}</h4>")
    print(f'<a href="{web_url}">{web_url}</a><br><br>')

print("</body></html>")
