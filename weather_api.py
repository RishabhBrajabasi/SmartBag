# Weather API 
# Project: Smart Bag
# Author: Rishabh Brajabasi
# Date: 28/02/2019

import requests
import json
import datetime
from datetime import timedelta
# OpenWeather API being used.
# AppID: 8575565e7b53238c795bbc5e6b4e54b6

current_api_address = "http://api.openweathermap.org/data/2.5/weather?appid=8575565e7b53238c795bbc5e6b4e54b6&q=Pittsburgh"
forecast_api_address = "http://api.openweathermap.org/data/2.5/forecast?appid=8575565e7b53238c795bbc5e6b4e54b6&zip=15217,us&units=metric"

json_data = requests.get(forecast_api_address).json()

#TODO:Make it dependent on current date, and not just on the first 4 entries.

#currentDT = datetime.datetime.now().replace(microsecond=0, second = 0);
#dayPlusOne = currentDT + timedelta(days = 1)
#print(str(currentDT))
#print(str(dayPlusOne))

# Jacket | Umberella | Bottle | Box | Folder_1 | Folder_2 | Folder_3
objectsNeeded = [0,0,0,0,0,0,0]
print(objectsNeeded)

#for dh in range(0,len(json_data["list"])):
for dh in range(0, 4):
#    if(json_data.get("list")[dh].get("main").get("temp")) is not None:
#        print(json_data.get("list")[dh].get("main").get("temp"))

# Check for jacket
    if(json_data.get("list")[dh].get("main").get("temp_min")) is not None:
        if(json_data.get("list")[dh].get("main").get("temp_min")) < 0.0:
            if(objectsNeeded[0] != 1):
                print("Jacket Needed")
                objectsNeeded[0] = 1

# Check for Umberella
    wc = (len((json_data.get("list")[dh].get("weather"))))
    if wc > 0:
        for w in range(0,wc):
            id = (json_data.get("list")[dh].get("weather")[w].get("id"))  
            if( id >= 200 and id < 800):
                if(objectsNeeded[1] != 1):
                    print("Umberella Needed")
                    objectsNeeded[1] = 1

print(objectsNeeded)

#TODO:Make it dependent on current date, and not just on the first 4 entries.
#    if(json_data.get("list")[dh].get("dt_txt") is not None):
#        predictedDT = json_data.get("list")[dh].get("dt_txt")
#        print(str(predictedDT))
#        print(type(predictedDT))
#        print(type(dayPlusOne))
#        if( predictedDT < dayPlusOne):
#            print("Days of our lives")
#            print(dh)




"""
    print("\n Date:")
    if(json_data.get("list")[dh].get("dt") is not None):
        print(json_data["list"][dh]["dt"])
    
    print("\n Main:")
    if(json_data.get("list")[dh].get("main") is not None):
        print(json_data["list"][dh]["main"])
    
    print("\n weather:")
    if(json_data.get("list")[dh].get("weather") is not None):
        print(json_data["list"][dh]["weather"])   
    
    print("\n clouds:")
    if(json_data.get("list")[dh].get("clouds") is not None):
        print(json_data["list"][dh]["clouds"])
    
    print("\n wind:")
    if(json_data.get("list")[dh].get("wind") is not None):
        print(json_data["list"][dh]["wind"])
    
    print("\n snow:")
    if(json_data.get("list")[dh].get("snow") is not None):
        print(json_data["list"][dh]["snow"])
    
    print("\n sys:")
    if(json_data.get("list")[dh].get("sys") is not None):
        print(json_data["list"][dh]["sys"])
    
    print("\n dt_txt:")
    if(json_data.get("list")[dh].get("dt_txt") is not None):
        print(json_data["list"][dh]["dt_txt"])
"""
