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
    [b.write_igrams_to_file(c[0], c[1], p) for c in settings.insta_static_coordinates_to_scan]
    # scan dynamic coordinates stored in the cache
    [b.write_igrams_to_file(c.strip(',')[0], c.strip(',')[1], p) for c in cache.get_all_keys(cache_obj)]


