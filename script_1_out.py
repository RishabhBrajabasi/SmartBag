from __future__ import print_function
import datetime
from datetime import timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time

import os
import requests
import json
import datetime
from datetime import timedelta
# OpenWeather API being used.
# AppID: 8575565e7b53238c795bbc5e6b4e54b6

current_api_address = "http://api.openweathermap.org/data/2.5/weather?appid=8575565e7b53238c795bbc5e6b4e54b6&q=Pittsburgh"
forecast_api_address = "http://api.openweathermap.org/data/2.5/forecast?appid=8575565e7b53238c795bbc5e6b4e54b6&zip=15217,us&units=metric"

json_data = requests.get(forecast_api_address).json()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

pathON = '../ObjectsNeeded.txt'

exists = os.path.isfile(pathON)
if(exists):
    on = open(pathON,"a+")
else:
    on = open(pathON,"w+")


# Jacket | Umbrella | Bottle | Box | Folder_1 | Folder_2 | Folder_3 | Headphones
objectsNeeded = [0,0,0,0,0,0,0,0]

def addObject(str):
    on = open(pathON, 'a+')
    contents = on.read()
    listContents = contents.split('|')[:-1];
    if(str in listContents):
        print("Object already in list")
    else:
        on.write(str+"|")
        print("Object added to list")
    on.close()

def schedule():
    # Boilerplate code to access Google calendar API
    
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Calculate current time and time interval of interest
    now = datetime.datetime.utcnow()
    future = now +timedelta(hours = 24)
    start = now.isoformat() + 'Z' # 'Z' indicates UTC time
    end = future.isoformat() + 'Z' # 'Z' indicates UTC time

    events_result = service.events().list(calendarId='primary', timeMin=start,timeMax=end,
                                        maxResults=50, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        eventStr = event['summary'].encode('ascii','ignore')
        if(eventStr == 'Networked Cyber-Physical Systems :: 18651 A'):
            if(objectsNeeded[4] != 1):
                addObject("Notebook1")
                objectsNeeded[4] = 1

        if(eventStr == 'Building User-Focused Sensing Systems :: 17722 A'):
            if(objectsNeeded[5] != 1):
                addObject("Notebook2")
                objectsNeeded[5] = 1

        if(eventStr == 'Wireless Sensor Networks :: 18748 A'):
            if(objectsNeeded[6] != 1):
                addObject("Notebook3")
                objectsNeeded[6] = 1

def weather():
    for dh in range(0, 4):
    # Check for jacket - Temperature
        if(json_data.get("list")[dh].get("main").get("temp_min")) is not None:
            if(json_data.get("list")[dh].get("main").get("temp_min")) < 20.0:
                if(objectsNeeded[0] != 1):
                    addObject("Jacket")                    
                    objectsNeeded[0] = 1

    # Check for Umbrella - Weather code
        wc = (len((json_data.get("list")[dh].get("weather"))))
        if wc > 0:
            for w in range(0,wc):
                id = (json_data.get("list")[dh].get("weather")[w].get("id"))  
                if( id >= 200 and id <= 800):
                    if(objectsNeeded[1] != 1):
                        addObject("Umbrella")
                        objectsNeeded[1] = 1

def alwaysNeeded():
    addObject("Box")
    addObject("Bottle")
    addObject("Headphones")

if __name__ == '__main__':
    while ( True ):
        hour = datetime.datetime.now().time().hour
        minute = datetime.datetime.now().time().minute
        if( (hour == 2 or hour == 12) and (minute == 34)):
            on = open(pathON, 'w+') # Clear the file
            on.close()
            schedule()
            weather()
            alwaysNeeded()
            time.sleep(61) # Make sure you wait long enough to not clear the file
            
