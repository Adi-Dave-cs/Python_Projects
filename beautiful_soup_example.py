from html.parser import HTMLParser
import urllib.error , urllib.request, urllib.parse
from bs4 import BeautifulSoup

print("Enter the url")
url = str(input())
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

#retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

    
