import datetime

# ID of the calendar to be used
CALENDAR_ID = "4824f6e23a9b27a085eb59931de25712868596f07beee0fec87e02ac1dd7ed64@group.calendar.google.com"

def retrieve(service):
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

    events_result = (
        service.events()
        .list(
            calendarId=CALENDAR_ID, # This is the test calendar
            timeMin=now, # UTC Time, gives only future events
            singleEvents=True, # Expands recurring events into separate instances rather than grouping them
            orderBy="startTime", # Sorted by start time in ascending order UTC
        )
        .execute()
    )

    events = events_result.get("items", [])
    return events

def add(name, startTime, endTime, service):
    event = {
        "summary": name,
        "start": {
            "dateTime": startTime,
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": endTime,
            "timeZone": "UTC",
        }
    }

    service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

def delete(event, service):
    service.events().delete(calendarId=CALENDAR_ID, eventId=event["id"]).execute()

