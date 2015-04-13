import urllib2
import re
import os
from bs4 import BeautifulSoup, SoupStrainer

f = urllib2.urlopen("https://www.google.com")
s = f.read()


# Write data to a temp files
ff = open("temp.html", "w")
ff.write(s)

# to get only 'a' tag of the page
soup = BeautifulSoup(s)
for tag in soup.find_all('a'):
 #tag['href'] = urlparse.urljoin(url, tag['href'])
 print tag

# finding links on a page with 're' package
# links = re.findall('"((http|ftp)s?://.*?)"', s)
# print links

f.close
os.remove("temp.html")