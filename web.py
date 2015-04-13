import urllib2
from bs4 import BeautifulSoup

f = urllib2.urlopen("https://www.google.com")
s = f.read()
print s
f.close()