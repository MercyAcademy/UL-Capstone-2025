import smtplib
import datetime
import configcreator
import os;
from email.mime.text import MIMEText
from dotenv import load_dotenv


subject = "Notice of Schedule Change"
body = "The door schedule has been changed"
sender = "yinzstudio@gmail.com"
recipients = configcreator.read_config()['mailinglist'].split(" ")
load_dotenv()
password = os.environ.get("GMAIL")


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
       smtp_server.ehlo()
       smtp_server.starttls()
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
       smtp_server.close()
    print("Message sent!")

def emailfromdoorchange(doorname, originalschedule,newschedule):
    Doorname = doorname
    ogdoorstatus = originalschedule['door_status']
    newdoorstatus = newschedule['door_status']
    starttime = newschedule['start_time'].strftime("%m/%d/%Y, %H:%M:%S")
    endtime = newschedule['end_time'].strftime("%m/%d/%Y, %H:%M:%S")

    msgbody = "The " + Doorname + (" door has changed from being ") + ogdoorstatus + " to " + newdoorstatus + " between the times of " + starttime + " and " + endtime + ". Changes are reflected in the calendar at https://calendar.google.com/calendar/u/0/r" 
    send_email(subject, msgbody, sender, recipients, password)

def emailmultipledoorchange():
    msgbody = "Multiple door schedules in your building have changed. The calendar is available at https://calendar.google.com/calendar/u/0/r."
    send_email(subject,msgbody,sender,recipients,password)
    
originalevent = {'door_status': 'unlocked', 'start_time': datetime.datetime(2025, 3, 20, 17, 30), 'end_time': datetime.datetime(2025, 3, 20, 19, 0)}
newevent = {'door_status': 'access_controlled', 'start_time': datetime.datetime(2025, 3, 21, 16, 30), 'end_time': datetime.datetime(2025, 3, 21, 17, 30)}

emailfromdoorchange("Atrium",originalevent,newevent)
