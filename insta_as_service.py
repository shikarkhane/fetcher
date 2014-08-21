from insta.insta_talker import Base
import settings
from common.pipeline import Pipe
from common import cache
from dogpile.cache import make_region
import time

def insta_service(cache_coordinates, cache_post_ids):
    b = Base(settings.insta_access_token)
    # scan static coordinates
    try:
        for c in settings.insta_static_coordinates_to_scan:
            b.write_igrams_to_file(c[0], c[1], cache_post_ids)
            time.sleep(settings.insta_sleep_between_calls_in_sec)
    except Exception as e:
        print str(e)
    # scan dynamic coordinates stored in the cache
    try:
        for c in cache.get_all_keys(cache_coordinates):
            b.write_igrams_to_file(c.split(',')[0], c.split(',')[1], cache_post_ids)
            time.sleep(settings.insta_sleep_between_calls_in_sec)
    except Exception as e:
        print str(e)


