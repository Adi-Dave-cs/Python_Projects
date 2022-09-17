from ossaudiodev import SOUND_MIXER_TREBLE
import ssl
from turtle import ht
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#ignore ssl certification
ctx =  ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = str(input("Enter url :- "))
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

# retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag)