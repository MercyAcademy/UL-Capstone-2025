import datetime

# ID of the calendar to be used
CALENDAR_ID = "4824f6e23a9b27a085eb59931de25712868596f07beee0fec87e02ac1dd7ed64@group.calendar.google.com"
eventColor = {"unlocked": "10", "locked": "11", "access_controlled": "8", "card_and_code": "5"} 

def retrieve(service):
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

    events_result = (
        service.events()
        .list(
            calendarId=CALENDAR_ID, # This is the test calendar
            timeMin=now, # UTC Time, gives only future events
            singleEvents=True, # Expands recurring events into separate instances rather than grouping them
            orderBy="startTime", # Sorted by start time in ascending order UTC
            fields="items(summary,id,description,start,end,colorId)"
        )
        .execute()
    )

    events = events_result.get("items", [])
    return events

def add(event, service):
    newEvent = {
        "summary": event["name"],
        "start": {
            "dateTime": (event["start_time"].isoformat() + "Z"),
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": (event["end_time"].isoformat() + "Z"),
            "timeZone": "UTC",
        },
        "description": event["door_status"],
        "colorId": eventColor[event["door_status"]]
    }

    service.events().insert(calendarId=CALENDAR_ID, body=newEvent).execute()

def delete(event, service):
    service.events().delete(calendarId=CALENDAR_ID, eventId=event["id"]).execute()

