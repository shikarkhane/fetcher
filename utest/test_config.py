'''
Created on Sep 29, 2013

@author: nikhil
'''
import unittest
import ConfigParser
import config

testkey = "check_test_config"
testvalue = "check_test_value"
class Test_config(unittest.TestCase):
    def setUp(self):
        config.create_config_file(testkey, testvalue)
    def tearDown(self):
        pass
    def test_append_to_file_one_line(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.cfg') 
        self.assertEqual(testvalue, config.get('Test', testkey))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()