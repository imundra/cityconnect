import urllib, json
from pprint import pprint

def getCityLatLong(inputCity):
    with open('cities.json') as data_file:    
        data = json.load(data_file)

    inp=inputCity
    inp=inp.strip().lower()
    found=False
    output=[]
    for x in data["cities"]:
        if x["city"].lower()==inp:
            #Latitude
            output.append(str(x["latitude"]))
            #Longitude
            output.append(str(x["longitude"]))
            output.append(str(x["state"]))
            found=True
            break
    if(not found):
        output.append("Info Not Found")
    
    output.append(x["city"])
    
    return output
