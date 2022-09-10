# REST APIs:
# https//:api.datamusr.com/words?rel_rhy=funny
# In the above example the https//: is the internet proticol and is secure because of the sc
# The api.datamusr.com/words is the baseurl
# The rel_rhy = funny is the parameter where the rel+rhy is the key and funny is the value
# You can stich together a url by sing the requests.get('baseurl',param = {key:value}) function or call a premade baseurl

import requests
def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    print(resp.url)
    return [d['word'] for d in word_ds]
    return resp.json() # Return a python object (a list of dictionaries in this case)

print(get_rhymes('moon'))
