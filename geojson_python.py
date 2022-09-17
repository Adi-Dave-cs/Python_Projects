import json
import urllib.request, urllib.parse, urllib.error 

# need to add the api key in order to access it


api = 'http://maps.googleapis.com/maps/api/geocode/json?'

while(True):
    url = str(input('Enter the location := '))
    if(len(url) < 1):
        break
    url = api+urllib.parse.urlencode({'address' : url})
    print("Retrieving url ..." ,url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved ",len(data),' characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failed to retrieve')
        print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    long = js["results"][0]["geometry"]["location"]["long"]
    print("Lat:= ",lat," Long:= ",long)
    location = js["results"][0]["formatted_address"]
    print(location)
