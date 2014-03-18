'''
Created on Mar 7, 2014

@author: nikhil
'''
import tornado.web
from common import cache

class Base_handler(tornado.web.RequestHandler):
    '''
    initiates different fetcher services to get data
    '''
    def initialize(self, my_shared_cache):
        self.my_shared_cache = my_shared_cache
    def get(self, q_lat, q_long):
        cache.get_or_create(self.my_shared_cache, q_lat, q_long)



