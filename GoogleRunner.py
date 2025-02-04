import datetime
import CalendarOperations
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SERVICE_ACCOUNT = "service_account.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def startup_creds():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT, scopes=SCOPES)
    return build("calendar", "v3", credentials=creds)

def main():
    try:
        service = startup_creds()
        calendar = CalendarOperations.retrieve(service)

        # --------
        # Here the logic will be programmed based on data from Verkada
        # --------

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
