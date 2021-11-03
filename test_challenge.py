### In this short time, I have tried to understand unit testing, and how its implemented using Pytest.
### I didn't had much idea regarding what sort of unit tests are you looking for and hence went on with writing unit
### tests that would help assess my earlier task. 
### This unit test would check if all the dictionary files for all races have relevant required data, is date time in correct format
### and is Regions consistently Australia
### let me know if you were looking for something else or want me to adapt this code in anyway
### I'll look forward to your feedback

# Importing relevant Python Libraries
import pytest
import json
import re
from operator import itemgetter

# Loading JSON file. Alternatively I can convert my challenge.py into a function and call it here
with open('./data.json','r') as jsonfile:
    results = json.loads(jsonfile.read())

# This test is written to makesure StartTime is presented in correct AEST ISO format for all races
@pytest.mark.parametrize("event", results)
def test_validate_timeFormat(event):
    pattern = re.compile(r'(\b[0-9]{4}\-[0-9]{2}\-[0-9]{2}T[0-9]{2}\:[0-9]{2}\:[0-9]{2}\b)')
    assert pattern.match(event['StartTime'])

# This test is to makesure all dictionaries of each race have required data, it would through an exception otherwise
@pytest.mark.parametrize("event", results)
def test_required_data(event):
    try:
        response = itemgetter('MeetingID', 'MeetingName', 'EventID', 'RaceNumber', 'RaceLink', 'Distance', 'StartTime')(event)
    except ValueError:
        print('Some of the required data is missing')

# This test is to make sure location is consistently Australia for all races
@pytest.mark.parametrize("event", results)
def test_location(event):
    assert event.get('Region') == 'Australia'
    
# You can test this code by just running "pytest" in root directory. 
    
# Console Output
#======================================================================= test session starts ========================================================================
#platform win32 -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
#rootdir: C:\coding challenge\CodingChallenge
#plugins: dash-1.12.0, hypothesis-5.5.4, arraydiff-0.3, astropy-header-0.1.2, doctestplus-0.5.0, openfiles-0.4.0, remotedata-0.3.2
#collected 657 items                                                                                                                                                  

#test_sample.py .............................................................................................................................................. [ 21%] 
#............................................................................................................................................................. [ 45%] 
#............................................................................................................................................................. [ 69%] 
#............................................................................................................................................................. [ 93%] 
#............................................                                                                                                                  [100%] 
#
#======================================================================= 657 passed in 2.45s ======================================================================== 
