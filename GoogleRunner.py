import os.path

from RetrieveCalendar import RetrieveCalendar
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Temporary Scope, it will need to be changed as this is readonly
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def main():
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Below will contain the calls from other files
    # This will include adding, removing, and retrieving the Calendar info

    RetrieveCalendar(service)

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
