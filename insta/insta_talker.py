from instagram.client import InstagramAPI
from common.utility import Coordinate_handler, Date_handler, File_handler
import json
import urllib2
import settings

class Igram():
    '''1. this class corresponds to the tipoff post structure, on the feeder side
    2. we will populate this class and then write json to flat files, making it convienent for logstash to consume it.
        Json example of a post:
{
               "text" => "@nollbit @johanni ja, klart det bara blir spekulationer. Men samhllsnyttig infrastruktur br vl vara delvis skyddad mot detta?",
               "lang" => "sv",
         "@timestamp" => "2014-01-09T10:01:30.449Z",
               "type" => "twitter",
            "post_id" => 418676219430047744,
           "up_votes" => 0,
       "user_mention" => "{\"id\"=>15809255, \"indices\"=>[0, 8], \"id_str\"=>\"15809255\", \"screen_name\"=>\"nollbit\", \"name\"=>\"johan\"},{\"id\"=>16311319, \"indices\"=>[9, 17], \"id_str\"=>\"16311319\", \"screen_name\"=>\"johanni\", \"name\"=>\"Johan Nilsson\"}",
         "place_name" => "Knivsta",
            "user_id" => "14235149",
       "user_img_url" => "http://pbs.twimg.com/profile_images/378800000478670862/88783a59c7c7e5c200627af584781212_normal.jpeg",
    "content_img_url" => "%{[entities][media_url]}",
              "coord" => "59.74596768,17.78693824"
}
    '''
    def __init__(self, post_id, text, created, content_img_url, user_img_url, user_id, place_name, coord, username, up_votes =0 ):
        # post_id is the internal _id of elasticsearch store
        #"user_id", "place_name", "text", "@timestamp", "type", "post_id", "user_img_url", "content_img_url", "coord", "up_votes", "username"
        self.post_id = post_id
        self.text = text
        self.created = created
        self.content_img_url = content_img_url
        self.user_img_url = user_img_url
        self.type = 'instagram'
        self.up_votes = up_votes
        self.user_id = user_id
        self.place_name = place_name
        self.coord = coord
        self.username = username
    def get_as_dict(self):
        d = {"post_id": self.post_id, "text": self.text, "created": self.created.strftime("%Y-%m-%dT%H:%M:%SZ"),
             "content_img_url": self.content_img_url, "user_img_url":self.user_img_url, "source": self.type, "up_votes": self.up_votes,
             "user_id": self.user_id, "place_name": self.place_name, "coord": self.coord, "username": self.username}
        return d
class Base():
    def __init__(self, access_token):
        self.token = access_token
        self.api = InstagramAPI(access_token=access_token)
    def get_closest_media_objects(self, lat, lon, min_timestamp):
        '''returns a list of media ids'''
        media = self.api.media_search(lat=lat, lng=lon, min_timestamp=min_timestamp)
        return media
    def make_igram(self, media_obj):
        o = media_obj
        post_id = o.id
        if o.caption:
            text = o.caption.text
        else:
            text = 'Check out my instagram!'
        created = o.created_time
        content_img_url = o.link
        user_img_url = o.user.profile_picture
        user_id = o.user.id
        username = o.user.username
        coord = "{0},{1}".format(o.location.point.latitude, o.location.point.longitude)
        if o.location.name:
            place_name = o.location.name
        else:
            place_name = Coordinate_handler().reverse_lookup_locality(coord)
        up_votes = o.like_count
        i = Igram(post_id, text, created, content_img_url, user_img_url, user_id, place_name, coord, username, up_votes)
        return i
    def get_staging_file(self):
        staging_file_path = settings.STAGING_RAW_FEED_FILE_PATH
        file_name_prefix = settings.insta_raw_feed_file_prefix
        self.staging_full_path = "{0}{1}{2}.txt".format(staging_file_path, file_name_prefix, Date_handler().get_current_utc_date_string("%Y%m%d_%H%M"))
        f = File_handler(self.staging_full_path)
        return f
    def write_igrams_to_file(self, lat, lon):
        min_timestamp = Date_handler().get_utc_x_minutes_ago(settings.insta_fetch_window_in_minutes)
        media_set = self.get_closest_media_objects(lat, lon, min_timestamp)
        igrams = [(self.make_igram(media)) for media in media_set]
        f = self.get_staging_file()
        [f.append_to_file_as_json(i.get_as_dict()) for i in igrams]
        f.copy_file_to(self.staging_full_path, settings.RAW_FEED_FILE_PATH)
