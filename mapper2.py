import googlemaps
import requests
import json
import pprint
import time
import pandas as pd
import csv

tokenList = []
file = csv.reader(open('latlng.csv'), delimiter=',')
tstamp = str(time.time())
gmaps = googlemaps.Client(key='AIzaSyDULVHPXxP19fwZdxDYAIbhzx7TM57PrPs')
i=0
for line in file:
    print(i)
    i+=1
    payload = {'key': 'AIzaSyDULVHPXxP19fwZdxDYAIbhzx7TM57PrPs','location':line[0]+ ',' +line[1],'radius':'50000','query': 'Coinme at Coinstar - Bitcoin Kiosk'}
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json',params = payload)
    data = r.json()
    x = 0
    w = open("newBTCCoinstarAddresses"+ tstamp +".csv","a")
    for z in data['results']:
        try:
            w.write(str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng'])+"\n")
            print(str(z['name'])+str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng']))
            x+=1
        except:
            print("WTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    w.close
    try:
        tokenList.append(data['next_page_token'])
    except:
        pass


tokenList2 = []
for i in tokenList:
    print(i)
    payload = {'key': 'AIzaSyDULVHPXxP19fwZdxDYAIbhzx7TM57PrPs','pagetoken':i}
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json',params = payload)
    data = r.json()
    x = 0
    w = open("newBTCCoinstarAddresses"+ tstamp +".csv","a")
    for z in data['results']:
        try:
            w.write(str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng'])+"\n")
            print(str(data['results'][x]['name'])+str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng']))
            x+=1
        except:
            print("WTFFFFFFFFFF")
    w.close
    try:
        tokenList2.append(data['next_page_token'])
    except:
        pass
tokenList3 = []
for i in tokenList2:
    print(i)
    payload = {'key': 'AIzaSyDULVHPXxP19fwZdxDYAIbhzx7TM57PrPs','pagetoken':i}
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json',params = payload)
    data = r.json()
    x = 0
    w = open("newBTCCoinstarAddresses"+ tstamp +".csv","a")
    for z in data['results']:
        try:
            w.write(str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng'])+"\n")
            print(str(data['results'][x]['name'])+str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng']))
            x+=1
        except:
            print("WTFFFFFFFFFF")
    w.close
    try:
        tokenList3.append(data['next_page_token'])
    except:
        pass

for i in tokenList3:
    print(i)
    payload = {'key': 'AIzaSyDULVHPXxP19fwZdxDYAIbhzx7TM57PrPs','pagetoken':i}
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json',params = payload)
    data = r.json()
    x = 0
    w = open("newBTCCoinstarAddresses"+ tstamp +".csv","a")
    for z in data['results']:
        try:
            w.write(str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng'])+"\n")
            print(str(data['results'][x]['name'])+str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng']))
            x+=1
        except:
            print("WTFFFFFFFFFF")
    w.close
    try:
        tokenList3.append(data['next_page_token'])
    except:
        pass
