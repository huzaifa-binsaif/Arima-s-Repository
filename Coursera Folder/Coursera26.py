# JSON represents data as nested 'lists' and 'dictionaries'
import json
data = ''' {
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

# Example:

import json
input = '''[
    {"id" : "001",
     "x" : "2",
     "name" : "Chuck"
     },
    {"id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''

info = json.loads(input)
print('User count', len(info))
for item in info:
    print('Name', item["name"])
    print('id', item["id"])
    print('Attribute', item["x"])

# It is time to create applications that help and work along side applications.
# APIs are aplication program interfaces.
# Example of using the google maps api:
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter Location: ")
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address':address})

    print("Retreving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrived", len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retriveve ====')
        print(data)
        continue
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
