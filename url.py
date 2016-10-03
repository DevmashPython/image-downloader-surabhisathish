import urllib
import re
url=raw_input("enter url:")
f=urllib.urlopen(url)
d=f.read()
a=re.compile('<img.*src="(.*\.jpg)"')
n=re.findall(a,d)
b=open("link1.txt","w")
for i in n:
		b.write(url+i+"\n")
b.close()