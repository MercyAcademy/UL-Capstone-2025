import configparser
import os
import logging 

def create_config():
    config = configparser.ConfigParser()

    config['General'] = {'testmode': False, 'Days_To_Schedule': 10}
    config['Google'] = {'groups': 'group_names'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    logging.log(os.getcwd())
    
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    debug_mode = config.getboolean('General', 'testmode')
    log_level = config.getint('General', 'Days_To_Schedule')
    db_name = config.get('Google', 'groups')

    config_values = {
        'testmode': debug_mode,
        'Days_To_Schedule': log_level,
        'groups': db_name,
    }

    return config_values

if __name__ == "__main__":
    create_config()
    print(read_config())
