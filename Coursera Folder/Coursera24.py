import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
# This is the object that is clean unlike messy html code
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
total = 0
for tag in tags:
    num = tag.contents[0]
    total = total + int(num)
print (total)
