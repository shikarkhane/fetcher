'''
Created on Sep 29, 2013

@author: nikhil
'''
import unittest
import os
import time
import json
import datetime
import settings

from common.pipeline import Pipe
from common.utility import File_handler, Date_handler, Coordinate_handler
from common import cache
from dogpile.cache import make_region

filename = "test_append_to_file_one_line.txt"
class Test_pipeline(unittest.TestCase):
    def setUp(self):
        self.p = Pipe()
        self.p.size = 1
    def test_add(self):
        new_id = '12345'
        self.p.add(new_id)
        self.assertEqual(self.p.add(new_id), False)
    def test_maintain(self):
        for i in range(10):
            self.p.add(i)
        self.p.size
        self.assertEqual(len(self.p.pipe), self.p.size)
class Test_utility(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_get_current_utc_string(self):
        e = datetime.datetime.now()
        expected = e.strftime(settings.UTC_TIMESTAMP_FORMAT)
        actual = Date_handler().get_current_utc_date_string(settings.UTC_TIMESTAMP_FORMAT)
        self.assertEqual(expected, actual)
    def test_append_to_file_as_json(self):
        #append current time to file 
        self.f = File_handler(filename)
        data = {"key" : "this could have been any kind of data. Doesnt have to be dictionary"}
        self.f.append_to_file_as_json(data)
        
        with open(filename, 'r') as testfile:
            all_lines = testfile.readlines()
        os.remove(filename)
        self.assertEqual(data, json.loads(all_lines[len(all_lines)-1]))
    def test_skip_this_data(self):
        accepting_country_codes = settings.TwitterStream_ACCEPTING_COUNTRY_CODES
        
        f = Coordinate_handler()
        coord_mixture = {"SE": [[16.59929221,59.92538324]]}
        for key in coord_mixture:
            for coord in coord_mixture[key]:
                data = { "time" : str(time.time()), "coordinates": {"coordinates": coord}}
                self.assertEqual(f.skip_this_data(data, accepting_country_codes), (False if key in accepting_country_codes else True))
    def test_find_country_codes_for_coord(self):
        f = Coordinate_handler()
        coord_mixture = {"SE": [[16.59929221,59.92538324]]}
        for key in coord_mixture:
            for coord in coord_mixture[key]:
                # data = { "time" : str(time.time()), "coordinates": {"coordinates": coord}}
                self.assertEqual(f.find_country_code_for_coordinates(coord), key)
class Test_cache(unittest.TestCase):
    def setUp(self):
        self.region = make_region().configure('dogpile.cache.memory')
    def test_add(self, lat=58, lng = 18):
        cache.get_or_create(self.region, lat, lng)
        r = self.region.get("{0},{1}".format(lat,lng))
        self.assertGreater(len(r), 0)
    def test_get_all_keys(self):
        coord_list = [[58,18],[57,17],[56,16],[55,15]]
        [self.test_add(i[0], i[1]) for i in coord_list]
        all_keys = cache.get_all_keys(self.region)
        self.assertEqual(len(all_keys), len(coord_list))
    def test_maintain(self):
        self.test_get_all_keys()
        cache.maintain(self.region)
        self.assertEqual(True, False)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()