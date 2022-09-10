import urllib.request, urllib.parse, urllib.error
import json
count = 0
total = 0
while True:
    url = input('Please enter the URL: ')
    if len(url)<1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    for item in js['comments']:
        count = count + 1
        total = total + item['count']
    print('Count:', count)
    print('Sum:', total)
    break
