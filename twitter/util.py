from twython import TwythonStreamer
from common.utility import File_handler
import ConfigParser

class Tweet_talker(TwythonStreamer):
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.cfg')
        self.file_path = config.get('General', 'raw_feed_file_path')
        
        super(Tweet_talker, self).__init__(config.get('General', 'consumer_key'), config.get('General', 'consumer_secret'),config.get('General', 'oauth_key'),config.get('General', 'oauth_secret'))
    def on_success(self, data):
        f = File_handler(self.file_path)
        f.append_to_file(str(data))

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()