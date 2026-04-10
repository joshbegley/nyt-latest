import os
import requests

API_KEY = os.environ.get("NYT_API_KEY", "")

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {"sort": "newest", "api-key": API_KEY}

r = requests.get(url, params=params)
data = r.json()

for doc in data["response"]["docs"]:
    if "cooking.nytimes.com" in doc["web_url"]:
        continue
    headline = doc["headline"]["main"]
    abstract = doc.get("abstract", "(No description)")
    web_url = doc["web_url"]
    print(f"**{headline}**\\")
    print(f"`{abstract}`\\")
    print(f"{web_url}\n")

