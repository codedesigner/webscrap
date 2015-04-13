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
# soup = BeautifulSoup(f)
# print soup.find_all('a')

links = re.findall('"((http|ftp)s?://.*?)"', s)
print links

f.close
os.remove("temp.html")