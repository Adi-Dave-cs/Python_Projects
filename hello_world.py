# first python file to print the hello world program
from codecs import charmap_build
import os 
print("--------------------hello world----------------")

p = "//!hello@!//"
print(p.lstrip('/'))
d = " hello World "
print(d.strip())
line = "Please have a nice days"
print(line.startswith("Please"))
print(line.startswith("Hello"))

d = dict()
for i in range(26):
    d[i] = i*5

print([sorted((v,k) for (k,v) in d.items())])


#Extracting host data from the line

d1 = "From golu@gmail.com hey wassup i am bholu@gmail.com"
pos = d1.find('@')
pos1 = d1.find(' ',pos)
d2 = d1[pos+1:pos1]
print(d2)
d = "Hello World"
d = d.strip()

for i in d:
    print(i,ord(i))