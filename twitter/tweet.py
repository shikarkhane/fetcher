'''
Created on Sep 26, 2013

@author: nikhil
'''
import tornado.web
from util import Tweet_talker

class Tweet_handler(tornado.web.RequestHandler):
    '''
    initiates twitter stream api to log data into flat files 
    '''
    def get(self):
        stream = Tweet_talker()
        #stream.statuses.filter(locations='14.776611,58.296405,19.742432,60.008507')
        stream.statuses.filter(track='badminton')
        