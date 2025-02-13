import configparser


def create_config():
    config = configparser.ConfigParser()

    # Add sections and key-value pairs
    config['General'] = {'testmode': False, 'Days_To_Schedule': 10}
    config['Google'] = {'groups': 'group_names'}

    # Write the configuration to a file
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    # Access values from the configuration file
    debug_mode = config.getboolean('General', 'testmode')
    log_level = config.getint('General', 'Days_To_Schedule')
    db_name = config.get('Google', 'groups')

    # Return a dictionary with the retrieved values
    config_values = {
        'testmode': debug_mode,
        'Days_To_Schedule': log_level,
        'groups': db_name,
    }

    return config_values

if __name__ == "__main__":
    create_config()
    print(read_config())