import os
import requests

API_KEY = os.environ.get("NYT_API_KEY", "")

url = "https://api.nytimes.com/svc/news/v3/content/all/all.json"
params = {"api-key": API_KEY}

r = requests.get(url, params=params)
data = r.json()

for doc in data["results"]:
    if "cooking.nytimes.com" in doc["url"]:
        continue
    headline = doc["title"]
    abstract = doc.get("abstract", "(No description)")
    web_url = doc["url"]
    print(f"**{headline}**\\")
    print(f"`{abstract}`\\")
    print(f"{web_url}\n")
