import httplib2
import json
import os
import urllib

from geopy.geocoders import Google, GeocoderDotUS

http = httplib2.Http()

def google(query):
    g = Google()
    try:
        place, (lat, lng) = g.geocode(query)
        return (lat, lng)
    except:
        return None, None

def geocoderdotus(query):
    us = GeocoderDotUS()
    try:
        place, (lat, lng) = us.geocode(query)
        return (lat, lng)
    except:
        return None, None

def yahoo(query):
    BASE = "http://where.yahooapis.com/geocode?"
    params = {
        'flags': 'JC', # JSON response, simplified
        'q': query,
        'appid': os.environ.get('YAHOO_APPLICATION_ID', '')
    }
    url = BASE + urllib.urlencode(params)
    r, c = http.request(url)
    c = json.loads(c)
    try:
        result = c['ResultSet']['Results'][0]
        return result['latitude'], result['longitude']
    except (KeyError, IndexError), e:
        print e
        return None, None