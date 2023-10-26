# API EXAMPLE - Google Maps API (doesn't work now as it asks for an API key)

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    location = input('Enter yout location: ')
    if len(location) < 1:
        break
    
    url = serviceurl + urllib.parse.urlencode({'address': location})
    print('Sending request to', url)
    url_handler = urllib.request.urlopen(url)
    data = url_handler.read().decode()
    print('Received', len(data), 'characters')

    try:
        json_data = json.loads(data)
    except:
        json_data = None
    
    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('Error')
        print(data)
        continue

# continue code ...
