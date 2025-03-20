import configparser
import os
import logging 

def create_config():
    config = configparser.ConfigParser()

    config['General'] = {'testmode': False, 'Days_To_Schedule': 10,'Setting 3': False,'Setting 4': False,'Setting 5': False}
    config['Google'] = {'groups': 'group_names','mailinglist': 'emails'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print(os.getcwd())
    
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    debug_mode = config.getboolean('General', 'testmode')
    log_level = config.getint('General', 'Days_To_Schedule')
    db_name = config.get('Google', 'groups')
    mailinglist = config.get('Google','mailinglist')
    config_values = {
        'testmode': debug_mode,
        'Days_To_Schedule': log_level,
        'groups': db_name,
        'mailinglist': mailinglist
    }

    return config_values

if __name__ == "__main__":
    print(read_config()['mailinglist'].split(" "))
