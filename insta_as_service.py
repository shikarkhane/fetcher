from insta.insta_talker import Base
import settings
from common.pipeline import Pipe
from time import sleep

# pipe object helps us check for duplicates
p = Pipe()
b = Base(settings.insta_access_token)
while True:
    b.write_igrams_to_file(59.328997,18.06549, p)
    sleep(settings.insta_fetch_window_in_minutes*61)
