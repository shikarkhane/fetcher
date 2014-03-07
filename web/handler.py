'''
Created on Mar 7, 2014

@author: nikhil
'''
import tornado.web

class Base_handler(tornado.web.RequestHandler):
    '''
    initiates different fetcher services to get data
    '''
    def get(self, q_lat, q_long):
        self.write("{0},{1}".format(q_lat, q_long))



