import requests
from bs4 import BeautifulSoup
import csv

url = ("https://www.nytimes.com/search?query=&sort=newest")

page = requests.get(url)
soup = BeautifulSoup(page, 'html.parser')

for a in soup.find_all("a",href=True):
	if "ResultPosition=" in a["href"]:
		if "cooking.nytimes.com" in a["href"]:
			pass
		else:
			cleaned_href = a["href"].split("?")[0]
			print ("**" + (a.h4.text.encode("utf-8")) + "**" + "\\")
			print ("`" + (a.p.text.encode("utf-8")) + "`" + "\\")
			print ("https://nytimes.com" + cleaned_href + "\n")
