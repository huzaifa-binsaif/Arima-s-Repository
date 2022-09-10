# It is time to create applications that help and work along side applications.
# APIs are aplication program interfaces.
# Example of using the google maps api:
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter Location: ")
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

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
    print(json.dumps(js, indent=4))
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
# This code would only work if you have access to the api key,
# That need to be bought so for now it is not something that we can play around
# and experement with exprement with.
# however some of it is still accessable without the api key
