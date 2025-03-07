import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.nytimes.com/search?query=&sort=newest"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

for a in soup.find_all("a", href=True):
    if "ResultPosition=" in a["href"]:
        if "cooking.nytimes.com" in a["href"]:
            continue
        
        cleaned_href = a["href"].split("?")[0]

        title = a.find("h4")
        description = a.find("p")

        title_text = title.text.encode("utf-8") if title else b"(No title)"
        description_text = description.text.encode("utf-8") if description else b"(No description)"

        print("**" + title_text.decode("utf-8") + "**" + "\\")
        print("`" + description_text.decode("utf-8") + "`" + "\\")
        print("https://nytimes.com" + cleaned_href + "\n")

