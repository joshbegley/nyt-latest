from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/search?query=a&sort=newest"

page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

for a in soup.find_all("a", href=True):
    if "ResultPosition=" in a["href"]:
        if "cooking.nytimes.com" not in a["href"]:
            cleaned_href = a["href"].split("?")[0]
            print("**" + a.h4.text + "**" + "\\")
            print("`" + a.p.text + "`" + "\\")
            print("https://nytimes.com" + cleaned_href + "\n")
