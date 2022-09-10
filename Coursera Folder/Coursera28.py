import urllib.request, urllib.parse, urllib.error
import twurl
import json

Twitter_url = 'https://api.twitter.con/1.1/friends/list.json'

while True:
    print('')
    acct = input('Enter Twitter Account: ')
    if (len(acct)<1): break
    url = twurl.argument(Twitter_url,
                          {'screen_name': acct, 'count': 5})
    print('Retrieving', url)
    connection = urllib.request.urlopen()
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('   ', s[:50])
