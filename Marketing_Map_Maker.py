import time
import hmac
import hashlib
import requests
import json
import string
import datetime as dt
from datetime import datetime
import pandas as pd
from os import path
import os
import folium
from jsondiff import diff
import base64
from io import BytesIO
from folium.plugins import MarkerCluster
from folium.features import CustomIcon
from pytrends.request import TrendReq
import pytrends

#This program takes the location data created by the Mapper_Final.py program and plots them on a map widget powered by folium
#This program cross references all previous iterations to isolate new locations as well as closures. New locations are then marked
#Also has a marketing map that utilizes the Google Trends API. This is meant to catch closures of business in areas where Google Trends is seeing an uptick in activity
#You may view a sample output of this program at Marketing_Map_2021-02-25.html  within github


class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

m = folium.Map(
    location=[33.8836365,-84.382076],
    zoom_start=12
    )

geoJson = "metroarea.json"

folium.GeoJson(
    geoJson,
    name='geojson'
).add_to(m)

marker_cluster = folium.plugins.MarkerCluster()
marker_cluster2 = folium.plugins.MarkerCluster()

marker_cluster2.add_to(m)
marker_cluster.add_to(m)
folium.LayerControl().add_to(m)


timestamp = str(round(time.time(),3))
public_key = 'ngizmtayzjmwyzgznzjhoduyyziymja'
secret_key = bytes('mzg1odq4mzzhn2rjzjbiztk2y2i3mzhjymrjntjmmwfhywfkotmzyziyma', 'utf-8')

payload = str(timestamp) + '|' + str(public_key)

digest = hmac.new(secret_key, payload.encode('utf-8'), hashlib.sha256).hexdigest()
filename = dt.date.today().strftime('%Y-%m-%d')+".json"

if not path.exists(filename):
    url = 'https://coinatmradar.com/operator-api/get/locationsinfo/'
    filename = dt.date.today().strftime('%Y-%m-%d')+".json"
    #headers = '{\'x-stamp\' : '+timestamp+', \'x-token\' : '+public_key+', \'x-signature\' : '+digest+'}'
    #jheaders = json.dumps(headers)
    #print(jheaders)

    catmrSession = requests.Session()
    res = catmrSession.get(url)
    cookies = dict(res.cookies)

    print(cookies)

    res = catmrSession.post(url,
    #    headers = {'content-type': 'application/json' },
        headers = {
            'x-stamp' : timestamp,
            'x-token' : public_key,
            'x-signature' : digest},
        cookies = cookies)



    f = open(filename, "w")
    f.write(res.text)
else:
    with open(dt.date.today().strftime('%Y-%m-%d')+".json") as json_file:
        data3 = json.load(json_file)
        if data3['is_success'] ==  0:
            print('BAD DATA')
        else:
            print('todays data is up to date')

with open(filename) as f:
    data = json.load(f)

with open('2020-12-15.json') as g:
    data2 = json.load(g)



i=0
weekAgo = time.time() - 604800*4
print(data)
for j in data['locations']:
    try:
        a = time.mktime(datetime.strptime(data['locations'][j]['installed'], "%Y-%m-%d").timetuple())
    except Exception as e:
        print(e)
    if a > weekAgo:
        print (datetime.utcfromtimestamp(a).strftime('%Y-%m-%d %H:%M:%S'))
        try:
            folium.Marker(
                location=[float(data['locations'][j]['lat']),float(data['locations'][j]['lng'])],
                icon= folium.features.CustomIcon(icon_image="new.png", icon_size=(41,38)),
                prefer_canvas=True
            ).add_to(marker_cluster2)
        except Exception as e:
            print(e)



data = data['locations']
z = 0
# print(data['data'])
# ok = pd.read_json(json.dumps(data['data']))
# print(umm[0])


#
# markerTypes = {
#     "Bitcoin Depot" : "icon",
#     "CoinFlip Bitcoin ATMs" : "icon",
#     "CoinCloud" : "icon",
#     "RockItCoin" : "icon",
#     "CoinSource" : "icon",
#     "Bitcoin of America" : "icon",
#     "National Bitcoin ATM" : "icon",
#     "Bitstop" :  "icon",
#     "Digital Mint" : "icon",
#     "ATM Coiners" : "icon",
#     "Athena Bitcoin" : "icon"
# }
#


for key, value in data.items():
    while z < 13000:
        html = "<style>\n div.a {text-align: center;\n}\n</style>\n<div class=\"a\"><h2>"+data[key]['business'] +"</h2></div><br><p style=\"text-align: left; width:24%; display: inline-block;\">Address:<br>Operator:<br>Install Date:<br>Hours:</p>\n<p style=\"text-align: right; width:75%;  display: inline-block;\">"+data[key]['address'].replace('\n',' ').replace(' USA','').replace('United States','')+"<br>"+str(data[key]['operator'])+"<br>"+data[key]['installed']+"<br>"+str(data[key]['hours']).replace('m S','m<br>S')+"</p>"

        # html = "<style>\n div.a {text-align: center;\n}\n</style>\n<div class=\"a\"><h2>"+data[key]['business'] +"</h2></div><br><p style=\"text-align:left;\">\n"+"Address:<br><p style=\"text-align:left;\">Operator:</p></p></span></span>"+"\n<span style=\"float:right;\">" + data[key]['address'].replace('\n',' ').replace(' USA','').replace('United States','')+"<br><span style=\"float:right;\">"+data[key]['operator']+"</span></span></p>"
        iframe = folium.IFrame(html)
        popup = folium.Popup(iframe, min_width=500, max_width=500)



        colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']

        print(os.getcwd())

        try:
            folium.Marker(
                location=[str(data[key]['lat']),str(data[key]['lng'])],
                popup= popup,
                icon= folium.features.CustomIcon(icon_image= data[key]['operator'] + " sprite.png", icon_size=(26,36)),
                prefer_canvas=True
            ).add_to(marker_cluster)
        except Exception as e:
            print(e)
            folium.Marker(
                location=[str(data[key]['lat']),str(data[key]['lng'])],
                popup= popup,
                icon= folium.Icon(color= colors[ord(data[key]['operator'][:1])*ord(data[key]['operator'][-2]) %19], icon='bitcoin', prefix='fa'),
                prefer_canvas=True
            ).add_to(marker_cluster)
        z += 1
        break

# Add effects to newly add items and delisted locationsinfo

# Compare json of today's data versus data from a week Agoura




    # for key, value in data[key].items():
    #      print("     "+ key + ":" + str(value))
    #      break


m.save('map'+dt.date.today().strftime(' %Y-%m-%d-%H-%M-%S')+'.html')
