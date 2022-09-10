import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
count = 0
repeat = 0
url = input('Enter - ')
while repeat < 4:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    # This is the object that is clean unlike messy html code
    soup = BeautifulSoup(html, 'html.parser')


    # Retrive all of the anchor tags
    # The ancher tags are all the contents rom <a to /a>
    tags = soup('a')
    print(tags)
    print('')
    for tag in tags:
        count = count + 1
        if count == 3:
            url = tag.get('href', None)
            repeat += 1
            break
