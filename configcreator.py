import configparser
import os
import logging 

def create_config():
    config = configparser.ConfigParser()

    config['General'] = {'testmode': False, 'Days_To_Schedule': 10,'Send_Emails': True,'Email_sender_address': "yinzstudio@gmail.com",'Setting 5': False}
    config['Google'] = {'groups': 'group_names','mailinglist': 'emails','emailimagepath': 'mercylogo.png'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print(os.getcwd())
    
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    debug_mode = config.getboolean('General', 'testmode')
    log_level = config.getint('General', 'Days_To_Schedule')
    Send_Emails = config.getboolean('General', 'send_emails')
    Email_sender_address = config.get('General','Email_sender_address')

    db_name = config.get('Google', 'groups')
    mailinglist = config.get('Google','mailinglist')
    emailimagepath = config.get('Google','emailimagepath')
    config_values = {
        'testmode': debug_mode,
        'Days_To_Schedule': log_level,
        'Send_Emails': Send_Emails,
        'Email_sender_address' : Email_sender_address,
        'groups': db_name,
        'mailinglist': mailinglist,
        'emailimagepath': emailimagepath
    }

    return config_values

if __name__ == "__main__":
    print(read_config())
