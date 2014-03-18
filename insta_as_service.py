from insta.insta_talker import Base
import settings
from common.pipeline import Pipe
from common import cache
from dogpile.cache import make_region

def insta_service(cache_obj):
    # pipe object helps us check for duplicates
    p = Pipe()
    b = Base(settings.insta_access_token)
    # scan static coordinates
    try:
        [b.write_igrams_to_file(c[0], c[1], p) for c in settings.insta_static_coordinates_to_scan]
    except:
        pass
    # scan dynamic coordinates stored in the cache
    try:
        [b.write_igrams_to_file(c.split(',')[0], c.split(',')[1], p) for c in cache.get_all_keys(cache_obj)]
    except:
        pass


