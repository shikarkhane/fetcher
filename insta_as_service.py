from insta.insta_talker import Base
import settings
from common.pipeline import Pipe
from time import sleep

def insta_service():
    # pipe object helps us check for duplicates
    p = Pipe()
    b = Base(settings.insta_access_token)
    [b.write_igrams_to_file(c[0], c[1], p) for c in settings.insta_static_coordinates_to_scan]
