import json
import pandas as pd

file_path = input("Enter your JSON file path ")
df = pd.read_json(r"response.json")

# load data using Python JSON module
with open(file_path,'r') as f:
    data = json.loads(f.read())
df_nested_list = pd.json_normalize(data, record_path =['dates'])

df_required = pd.json_normalize(
    data, 
    record_path =['dates'], 
      meta=[
        ['sections', 'raceType'], 
        ['sections', 'meetings', 'id'],
          ['sections', 'meetings', 'name'],
          ['sections', 'meetings', 'events','raceNumber'],
          ['sections', 'meetings', 'events','httpLink'],
          ['sections', 'meetings', 'events','id'],
          ['sections', 'meetings', 'events','distance'],
          ['sections', 'meetings', 'events','startTime'],
    ],errors='ignore'
)
