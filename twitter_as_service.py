# creating an option to run fetcher as a service as it would be lighter than running tornado
from twitter.tweet_talker import Tweet_talker
import time

stream = Tweet_talker()

while True:
    try:
        stream.statuses.filter(locations='-180,-90,180,90')
    except Exception as e:
        print str(e)
        # sleep for a min before trying again
        time.sleep(60)
