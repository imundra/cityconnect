MyKey = 'AIzaSyDVwV3ayl5QkMWzn6CvmkfjQUwvB3jLX08'
MyType = 'theater'

import urllib, json
from pprint import pprint

#Grabbing and parsing the JSON data
def GoogPlac(lat,lng,radius,types,key):
  #making the url
  AUTH_KEY = key
  LOCATION = str(lat) + "," + str(lng)
  RADIUS = radius
  TYPES = types
  MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
  #grabbing the JSON result
  response = urllib.urlopen(MyUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  return jsonData

#This is a helper to grab the Json data that I want in a list
def IterJson(place):
    x=[]
    
    try:
        x.append(place['name'])
    except:
        x.append("No Name Info")
        
    try:
        x.append(place['geometry']['location']['lat'])
    except:
        x.append("No Latitude Info")

    try:
        x.append(place['geometry']['location']['lng'])
    except:
        x.append("No Longitude Info")

    try:
        x.append(place['vicinity'])
    except:
        x.append("No Address Info")

    try:
        x.append(place['place_id'])
    except:
        x.append("No ID Info")

    try:
        x.append(place['photos'])
    except:
        x.append("No Photos Info")

    try:
        x.append(place['price_level'])
    except:
        x.append("No Price Level Info")

    try:
        x.append(place['rating'])
    except:
        x.append("No Rating Info")
        
    return x

def getNearbyData(lat, lon, radius, MyType, MyKey):
  testing=GoogPlac(lat, lon, radius, MyType, MyKey)
  allResults=[]
  for x in testing['results']:
      eachResult=[]
      output=IterJson(x)
      eachResult.append("Place: " + str(output[0].encode('ascii', 'ignore')))
      eachResult.append("Latitude: " + str(output[1]))
      eachResult.append("Longitude: " + str(output[2]))
      eachResult.append("Address: " + str(output[3].encode('ascii', 'ignore')))
      eachResult.append("Price Level: " + str(output[6]))
      eachResult.append("Rating: " + str(output[7]))
      allResults+=[eachResult]
  return allResults
