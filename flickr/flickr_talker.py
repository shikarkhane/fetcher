import flickrapi
from common.utility import Coordinate_handler, Date_handler, File_handler
import settings
from common.content import Post

class Base():
    def __init__(self, access_token):
        self.token = access_token
        self.api = flickrapi.FlickrAPI(self.token)
    def get_media_objects_in_bbox(self, bbox, min_timestamp):
        '''returns xmlnode with photo ids

        '''
        r = self.api.photos_search(min_taken_date=min_timestamp, accuracy='11', privacy_filter='1',
                                   bbox=bbox)
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
        i = Post(post_id, text, created, content_img_url, user_img_url, user_id, place_name, coord, username, 'instagram', up_votes)
        return i
    def get_staging_file(self):
        staging_file_path = settings.STAGING_RAW_FEED_FILE_PATH
        file_name_prefix = settings.insta_raw_feed_file_prefix
        self.staging_full_path = "{0}{1}{2}.txt".format(staging_file_path, file_name_prefix,
                                                        Date_handler().get_current_utc_date_string(settings.UTC_TIMESTAMP_FORMAT))
        f = File_handler(self.staging_full_path)
        return f
    def write_flickrs_to_file(self, bbox):
        min_timestamp = Date_handler().get_utc_x_minutes_ago(settings.flickr_fetch_window_in_minutes)
        media_set = self.get_closest_media_objects(lat, lon, min_timestamp)
        igrams = [(self.make_igram(media)) for media in media_set]
        f = self.get_staging_file()
        [f.append_to_file_as_json(i.get_as_dict()) for i in igrams]
        f.copy_file_to(self.staging_full_path, settings.RAW_FEED_FILE_PATH)

