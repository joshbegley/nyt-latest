import urllib2
from bs4 import BeautifulSoup
import csv

print "<html><head><style>h4{margin:0;font-weight:300;}</style></head>"
url = ("https://www.nytimes.com/search?query=&sort=newest")

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

for a in soup.find_all("a",href=True):
	if "ResultPosition=" in a["href"]:
		print (a.h4)
		print ("<a href=\"https://nytimes.com{}".format(a.attrs['href']))
		print "\">"
		print "https://nytimes.com{}".format(a.attrs['href'])
		print "</a><br><br>"
print "</html>"