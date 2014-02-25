# this file should contain only path related setttings
import os
DEBUG = True
DIRNAME = os.path.dirname(__file__)
RESOURCE_PATH = os.path.join(DIRNAME, 'resource')
GDAL_SHAPE_FILENAME = 'TM_WORLD_BORDERS-0.3.shp'
PIPELINE_SIZE = 1000

STAGING_RAW_FEED_FILE_PATH = '/home/nikhil/temp/feed/staging/'
RAW_FEED_FILE_PATH = '/home/nikhil/temp/feed/'

twitter_raw_feed_file_prefix = 'twitter_se_'
twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_oauth_key = ''
twitter_oauth_secret = ''
TwitterStream_ACCEPTING_COUNTRY_CODES = """['SE']"""

insta_client_id = ''
insta_client_key = ''
insta_access_token = ''
insta_raw_feed_file_prefix = 'insta_se_'
insta_fetch_window_in_minutes = 10

flickr_client_id = ''
flickr_client_key = ''
flickr_raw_feed_file_prefix = 'flickr_se_'
flickr_fetch_window_in_minutes = 10