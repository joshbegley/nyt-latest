import urllib2
from bs4 import BeautifulSoup
import csv

print "Headline | URL"
print "--- | ---"
url = ("https://www.nytimes.com/search?query=&sort=newest")

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

for a in soup.find_all("a",href=True):
	if "ResultPosition=" in a["href"]:
		if "cooking.nytimes.com" in a["href"]:
			pass
		else:
			print (a.h4.text.encode("utf-8")) + " | `" + ("https://nytimes.com{}".format(a.attrs['href']) + "`")