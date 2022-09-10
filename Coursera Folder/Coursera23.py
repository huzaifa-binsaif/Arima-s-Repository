import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def scraper():
    a = input('Enter count: ')
    b = int(input('Enter position: '))
    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    # This is the object that is clean unlike messy html code
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for i in range(0,int(a)):
        print(url)
        count = 0
        for tag in tags:
            count += 1
            if count < b:
                continue
            if count == b:
                url = tag.get('href', None)
                html = urllib.request.urlopen(url, context=ctx).read()
                soup = BeautifulSoup(html, 'html.parser')
                tags = soup('a')
                break
    return url
tag = scraper()
print(tag)
