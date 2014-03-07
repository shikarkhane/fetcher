# only static config values, which need a server restart should be written here
import os
DEBUG = True
DIRNAME = os.path.dirname(__file__)
RESOURCE_PATH = os.path.join(DIRNAME, 'resource')
GDAL_SHAPE_FILENAME = 'TM_WORLD_BORDERS-0.3.shp'
PIPELINE_SIZE = 1000

STAGING_RAW_FEED_FILE_PATH = '/home/nikhil/temp/feed/staging/'
RAW_FEED_FILE_PATH = '/home/nikhil/temp/feed/'

UTC_TIMESTAMP_FORMAT = "%Y%m%d_%H%M"

cache_key_expiry_in_days = 1
cache_get_all_keys_for_last_x_days = 10

twitter_raw_feed_file_prefix = 'twitter_se_'
TwitterStream_ACCEPTING_COUNTRY_CODES = """['SE']"""

insta_raw_feed_file_prefix = 'insta_se_'
insta_fetch_window_in_minutes = 1
insta_static_coordinates_to_scan = [[59.328997,18.06549]]

flickr_raw_feed_file_prefix = 'flickr_se_'
flickr_fetch_window_in_minutes = 10

twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_oauth_key = ''
twitter_oauth_secret = ''

insta_client_id = ''
insta_client_key = ''
insta_access_token = ''

flickr_client_id = ''
flickr_client_key = ''
