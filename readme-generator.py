import urllib2
from bs4 import BeautifulSoup
import csv

url = ("https://www.nytimes.com/search?query=a&sort=newest")

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

for a in soup.find_all("a",href=True):
	if "ResultPosition=" in a["href"]:
		if "cooking.nytimes.com" in a["href"]:
			pass
		if "/list/" in a["href"]:
			pass
		else:
			print ("**" + (a.h4.text.encode("utf-8")) + "**" + "\\")
			print ("`" + (a.p.text.encode("utf-8")) + "`" + "\\")
			print ("https://nytimes.com{}".format(a.attrs['href'])) + "\n"
