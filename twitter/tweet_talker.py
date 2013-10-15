from twython import TwythonStreamer
from common.utility import File_handler, Date_handler, Coordinate_handler
import ConfigParser

class Tweet_talker(TwythonStreamer):
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.cfg')
        self.file_path = config.get('General', 'raw_feed_file_path')
        self.accepting_country_codes = config.get('DataStream', 'ACCEPTING_COUNTRY_CODES')
        self.file_name = config.get('General', 'raw_feed_file_prefix') + Date_handler().get_current_utc_date_string("%Y%m%d_%H%M") + ".txt"
        
        self.country_code_handle = Coordinate_handler()
        self.file_handle = File_handler(self.file_path + self.file_name)  
        
        super(Tweet_talker, self).__init__(config.get('General', 'consumer_key'), config.get('General', 'consumer_secret'),config.get('General', 'oauth_key'),config.get('General', 'oauth_secret'))
    def on_success(self, data):
        if data:
            if not self.country_code_handle.skip_this_data(data, self.accepting_country_codes):
                self.file_handle.append_to_file_as_json(data)
    def on_error(self, status_code, data):
        print "Error code:{0}, Message:{1}".format(status_code, data)
        self.disconnect()