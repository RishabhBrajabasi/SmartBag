from __future__ import print_function
import datetime
from datetime import timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Need to have a credentials.json file to access the calendar


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


# Jacket | Umberella | Bottle | Box | Folder_1 | Folder_2 | Folder_3
objectsNeeded = [0,0,0,0,0,0,0]


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

    print('Getting events in the next 24 hours')
    events_result = service.events().list(calendarId='primary', timeMin=start,timeMax=end,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        eventStr = event['summary'].encode('ascii','ignore')
        if(eventStr == 'Networked Cyber-Physical Systems :: 18651 A'):
            if(objectsNeeded[4] != 1):
                print('18651')
                objectsNeeded[4] = 1

        if(eventStr == 'Building User-Focused Sensing Systems :: 17722 A'):
            if(objectsNeeded[5] != 1):
                print('17722')
                objectsNeeded[5] = 1

        if(eventStr == 'Wireless Sensor Networks :: 18748 A'):
            if(objectsNeeded[6] != 1):
                print('18748')
                objectsNeeded[6] = 1

    print(objectsNeeded)
if __name__ == '__main__':
    schedule()
