'''
Created on Sep 29, 2013

@author: nikhil
'''
import unittest
import os
import time
import json
import datetime
import ConfigParser

from common.utility import File_handler, Date_handler, Coordinate_handler

filename = "test_append_to_file_one_line.txt"

class Test_utility(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_get_current_utc_string(self):
        e = datetime.datetime.now()
        expected = e.strftime("%Y-%m-%d %H:%M")
        actual = Date_handler().get_current_utc_date_string("%Y-%m-%d %H:%M")
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
        config = ConfigParser.RawConfigParser()
        config.read('config.cfg')
        accepting_country_codes = config.get('DataStream', 'ACCEPTING_COUNTRY_CODES')
        
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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()