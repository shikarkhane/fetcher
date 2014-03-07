'''
Created on Feb 13, 2014

@author: nikhil
'''
import tornado.web
import settings

class Insta_handler(tornado.web.RequestHandler):
    '''
    list of coordinates for which we need to collect data from instagram
    '''
    def get(self):
        print settings.insta_coord_list



