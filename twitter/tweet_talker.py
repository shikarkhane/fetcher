from twython import TwythonStreamer
from common.utility import File_handler, Date_handler, Coordinate_handler
import settings as s

class Tweet_talker(TwythonStreamer):
    def __init__(self):
        self.staging_file_path = s.STAGING_RAW_FEED_FILE_PATH
        self.file_path = s.RAW_FEED_FILE_PATH
        self.accepting_country_codes = s.TwitterStream_ACCEPTING_COUNTRY_CODES
        self.file_name_prefix = s.twitter_raw_feed_file_prefix
        
        self.last_full_path = "{0}{1}{2}.txt".format(self.staging_file_path, self.file_name_prefix, Date_handler().get_current_utc_date_string("%Y%m%d_%H%M"))
        self.last_file_handle = File_handler(self.last_full_path)
         
        self.country_code_handle = Coordinate_handler()        
        super(Tweet_talker, self).__init__(s.twitter_consumer_key, s.twitter_consumer_secret, s.twitter_oauth_key,s.twitter_oauth_secret)
    def on_success(self, data):
        if data:
            if not self.country_code_handle.skip_this_data(data, self.accepting_country_codes):
                staging_full_path = "{0}{1}{2}.txt".format(self.staging_file_path, self.file_name_prefix, Date_handler().get_current_utc_date_string("%Y%m%d_%H%M"))
                if (self.last_full_path == staging_full_path):
                    handle_to_use = self.last_file_handle
                else:
                    # rollover file and copy over the old file to permanant location
                    handle_to_use = File_handler(staging_full_path)
                    handle_to_use.copy_file_to(self.last_full_path, self.file_path)
                    #reset last path and handle
                    self.last_full_path = staging_full_path
                    self.last_file_handle = handle_to_use
                self.last_file_handle.append_to_file_as_json(data)
    def on_error(self, status_code, data):
        print "Error code:{0}, Message:{1}".format(status_code, data)
        self.disconnect()