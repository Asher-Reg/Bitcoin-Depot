import googlemaps
import requests
import json
import pprint
import time
import pandas as pd
import csv
from datetime import datetime

#This program uses the Google Maps API to retrieve a list of all business addresses related to a keyword within a specified area
#Must feed in the list of cities to scrape in a csv file with the lat,lng of the cities
#Acts as a radar search of the list of lat,lng coordinates provided

file = csv.reader(open('latlng.csv'), delimiter=',')
today = datetime.today()
file_date= str(today.month) + "-" +str(today.day) +"-"+ str(today.year)
key='AIzaSyARtr8QgIH_54QifoouGDgYHPxRdj3vyeQ'

def radarsearch(keyword,lat,lng,**kwargs):
    if(kwargs):
        time.sleep(2)
        payload = {'key': key,'pagetoken':kwargs['token']}
    else:
        print("first iteration")
        payload = {'key': key,'location':lat+ ',' +lng,'radius':'50000','query': keyword}
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json',params = payload)
    data = r.json()
    x = 0
    w = open("G_Maps_Search_"+keyword+"_"+file_date+".csv","a")
    for z in data['results']:
        try:
            w.write(str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng'])+"\n")
            print(str(z['name'])+str(data['results'][x]['formatted_address'])+'|'+ str(data['results'][x]['geometry']['location']['lat']) +"|"+ str(data['results'][x]['geometry']['location']['lng']))
            x+=1
        except:
            print("Error retreiving data for" + lat + ", "+ lng)
    w.close
    try:
        token = data['next_page_token']
        print(token)
        radarsearch(keyword,lat,lng,token=token)
    except:
        print("ended")
        pass



for line in file:
    print(line)
    lat = line[0]
    lng = line[1]
    radarsearch('CoinMe',lat,lng)
    time.sleep(4)




