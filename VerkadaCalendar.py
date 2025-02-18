import json
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Creates the initial token and logs in using the api key, returns the newly opened session
def initialSetup():
    load_dotenv()
    api_key = os.environ.get("API_KEY")
    session = requests.Session()
    session.headers.update({"accept": "application/json", "x-api-key": api_key})
    response = session.post("https://api.verkada.com/token")
    token = response.text
    session.headers.update({"x-verkada-auth": token.split('"')[3]})
    return session

# Retrieves the exception calendar IDs for every door
def retrieveExceptionIDs(session):
    response = session.get("https://api.verkada.com/access/v1/door/exception_calendar")
    doorsJson = json.loads(response.text)
    doors = doorsJson.get("door_exception_calendars", [])
    return doors

# Returns a dictionary where the key is the name of the door and the value is a number of dictionaries for each day that has an exception
def dataFromCalendar(door, session):
    dictsFiltered = {}

    # Loops over all the days in the exceptions key
    for doorExceptions in door.get("exceptions", []):
        singleDict = {}
        
        # Retrieves the info for date, door_status, end_time, and start_time
        for key in {"door_status", "end_time", "start_time"}:
            if key in doorExceptions:
                if key == "start_time" or key == "end_time":
                    singleDict[key] = datetime.strptime(doorExceptions["date"] + " " + doorExceptions[key], "%Y-%m-%d %H:%M:%S")

                else:
                    singleDict[key] = doorExceptions[key]

                name = door.get("name")

                if name not in dictsFiltered:
                    dictsFiltered[name] = []
                
                dictsFiltered[name].append(singleDict)

        return dictsFiltered

# The main function that returns all the doors calendars in a dictionary
def retrieveCalendar():
    session = initialSetup()
    doors = retrieveExceptionIDs(session)
    allDoorsCalendars = {}

    # Loops through every door calendar to create one large dictionary containg all info
    for door in doors:
        callDict = dataFromCalendar(door, session)   
        
        if callDict:
            doorKey = next(iter(callDict))
            allDoorsCalendars[doorKey] = callDict[doorKey]

    return allDoorsCalendars

if __name__ == "__main__":
    print(retrieveCalendar())
