# creating an option to run fetcher as a service as it would be lighter than running tornado
import config
from twitter.tweet_talker import Tweet_talker

config.create_config_file("mainkey","mainvalue")

stream = Tweet_talker()
stream.statuses.filter(locations='-180,-90,180,90')
