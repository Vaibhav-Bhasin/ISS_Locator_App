import requests
URL = "http://api.open-notify.org/iss-now.json"
response=requests.get(URL)
response.status_code#this is just for telling , if we are able to enter the website , if its 200 then we are able to enter the website and if its 404 we are not able to enter it
data=response.json()#json (JavaScriptObjectNotation) this function json data to dic
print(data)
print(type(data))
iss_position=(data.get("iss_position"))
print(iss_position.get("longitude"))
import requests
import datetime
#Longitude:Your longitude
#Latitude:Your Latitude
#You can find it on: https://www.latlong.net/Show-Latitude-Longitude.html

user = input("Enter Your Current Latitude and Longitude::\n").split()

Latitude= user[0]
Longitude= user[1]

URL = f"https://api.n2yo.com/rest/v1/satellite/radiopasses/25544/Lat/Long/0/{Latitude}/{Longitude}/&apiKey=K58RAG-QVDW3U-H437K8-4QI0"
response = requests.get(URL)
data=response.json()
print(data)

for i in range(data["info"]["passescount"]):
  t = data["passes"][i]["startUTC"]
  print(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))


#Unix time for the start of this pass. You should convert this UTC value to observer's time zone

import datetime

t = datetime.datetime.now()
print(t)

