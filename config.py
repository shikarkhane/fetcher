import ConfigParser

def create_config_file(testkey, testvalue):
    config = ConfigParser.RawConfigParser()
    
    # When adding sections or items, add them in the reverse order of
    # how you want them to be displayed in the actual file.
    # In addition, please note that using RawConfigParser's and the raw
    # mode of ConfigParser's respective set functions, you can assign
    # non-string values to keys internally, but will receive an error
    # when attempting to write to a file or when you get it in non-raw
    # mode. SafeConfigParser does not allow such assignments to take place.
    config.add_section('Test')
    config.set('Test', testkey, testvalue)
    
    config.add_section('General')
    config.set('General', 'STAGING_RAW_FEED_FILE_PATH', '/home/nikhil/temp/feed/staging/')
    config.set('General', 'RAW_FEED_FILE_PATH', '/home/nikhil/temp/feed/')
    config.set('General', 'raw_feed_file_prefix', 'twitter_se_')
    config.set('General', 'consumer_key', '')
    config.set('General', 'consumer_secret', '')
    config.set('General', 'oauth_key', '')
    config.set('General', 'oauth_secret', '')
    
    config.add_section('DataStream')
    config.set('DataStream', 'ACCEPTING_COUNTRY_CODES', """['SE']""")
    
    # Writing our configuration file to 'example.cfg'
    with open('config.cfg', 'wb') as configfile:
        config.write(configfile)