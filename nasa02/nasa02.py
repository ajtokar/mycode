#!/usr/bin/env python3

#import urllib.request
#import json
import requests

#neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
#startdate = 'start_data=2018-06-01'
#enddate = '&end_date=END_DATE'
#mykey = '&api_key=vguqMrccGJX1FIITP7PDBy7PLw7YiFiib6gVB8Pf'

#neourl = neourl + startdate + mykey

#neourlobj = urllib.request.urlopen(neourl)

#neoread = neourlobj.read()

#decodeneo = json.loads(neoread.decode('utf-8'))

#print("\n\nConverted python data")
#print(decodeneo)

def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=vguqMrccGJX1FIITP7PDBy7PLw7YiFiib6gVB8Pf'

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

main()
