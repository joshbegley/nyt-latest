import urllib2
from bs4 import BeautifulSoup
import csv

print ("<html><head><style>html,body,p,h4{margin:0;font-family:avenir;font-weight:normal;font-size:1em;line-height:1.4em}a{font-size:0.8em;}h4{font-size:1.6em;}body{margin-left:20px}</style></head>")
url = ("https://www.nytimes.com/search?query=+")

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

for a in soup.find_all("a",href=True):
	if "ResultPosition=" in a["href"]:
		if "cooking.nytimes.com" in a["href"]:
			print("<br>")
		else:
			print (a.h4)
			print ("<a href=\"https://nytimes.com{}".format(a.attrs['href']) + "\">" + "https://nytimes.com{}".format(a.attrs['href']) + "</a><br><br>")
print ("</html>")
