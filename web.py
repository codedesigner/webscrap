import urllib2
import re
import os
from bs4 import BeautifulSoup, SoupStrainer

# Function to parse webpage
def parse_webpage() :
    f = urllib2.urlopen("https://www.google.com")
    s = f.read()
    f.close
    return s

# Function to write data to a file
def save_webpage() :
    # Write data to a temp files
    ff = open("temp.html", "w")
    ff.write(s)

# Function to get all links from current page
def get_all_links_from_webpage() :
    # get the webpage to collect all the links on it
    
    # to get only 'a' tag of the page
    soup = BeautifulSoup(parse_webpage())
    for tag in soup.find_all('a'):
        print tag
    
# Deleting the temp file
#os.remove("temp.html")