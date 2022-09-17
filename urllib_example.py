from logging import FileHandler
import urllib.request, urllib.parse , urllib.error

print("Enter the url of the site you would like to open")
url = str(input())
fhand = urllib.request.urlopen(url)
# fwrt = open('example.txt','w')
count = dict()

for line in fhand:
    # fwrt.write(line.decode().strip())
    print(line.decode().strip())
    line = line.strip()
    words = line.split()
    for word in words:
        count[word] =  count.get(word,0)+1

print(count)
# fwrt.close()