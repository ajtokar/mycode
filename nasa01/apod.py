#!/usr/bin/env python3

import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=vguqMrccGJX1FIITP7PDBy7PLw7YiFiib6gVB8Pf'

apodurlobj = urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))

print("\n\nConverted python data")
print(decodeapod)

input('\nPress Enter to open NASA Picture of the day in Firefox')
webbrowser.open(decodeapod['url'])
