import requests

r= requests.get('https://api.datamuse.com/words', params ={'rel_rhy':'moon'})
print (r.text)
print (r.url)

# This function can be use to create a url without the program trying to fetch it
# This is very useful in debugging when the requests.get does not output a url

import requests
def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url

r = requests.get('http://www.google.com/search', params = {'tbm':'isch','q':'violens and guitars'})
requestURL('https://www.google.com/search', params =  {'tbm':'isch','q':'violens and guitars'})
print(r.text)
print(r.url)
