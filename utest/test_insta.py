'''
Created on Feb 13, 2014

@author: nikhil
'''
import unittest
from insta.insta_talker import Base
import settings
import json

class Test_insta_talker(unittest.TestCase):
    def setUp(self):
        self.access_token = settings.insta_access_token
    def tearDown(self):
        pass
    def test_get_nearest_media(self):
        media = Base(access_token=self.access_token).get_closest_media_objects(lat=58.58972357,lon=16.19912264)
        self.assertGreater(len(media), 0)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()