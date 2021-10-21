#Importing important libraries
import pandas as pd
import json
from datetime import datetime, timedelta

#Asking user to input path to JSON file
file_path = input("Enter your JSON file path ")

#Loading JSON file
with open(file_path,'r') as f:
    data = json.loads(f.read())

#Gathering requirements
df_required = pd.io.json.json_normalize(
    data, 
    record_path =['dates',"sections","meetings","events"],
    meta = [["dates", "sections", "meetings", "id"],
           ["dates","sections","meetings","name"],
           ["dates", "sections", "meetings", "regionName"]
           ]
)

#Selecting needed columns
df = df_required[['dates.sections.meetings.regionName','dates.sections.meetings.id','dates.sections.meetings.name','id','raceNumber','httpLink','distance','startTime']]

#changing time zone to Australia/Brisbane and AEST iso formatting
df['startTime'] = pd.to_datetime(df['startTime'], unit='s')
df['startTime'] = df['startTime'] + timedelta(hours=10, minutes=0)
df['startTime'] = df['startTime'].dt.strftime('%Y-%m-%dT%H:%m:%S')

#Renaming columns and droping unnecessary data
df.columns = ["Region", "MeetingID", "MeetingName", "EventID", "RaceNumber", "RaceLink", "Distance", "StartTime"]
result = df[df['Region'] == 'Australia']
result.drop(['Region'], axis=1, inplace=True)

#Required dictionary
dict = result.to_dict('records')

print(dict)
