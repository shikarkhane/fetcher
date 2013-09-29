'''
Created on Sep 29, 2013

@author: nikhil
'''
import unittest
import os
import time

from common.utility import File_handler

filename = "test_append_to_file_one_line.txt"

class Test_utility(unittest.TestCase):
    def setUp(self):
        self.f = File_handler(filename)
    def tearDown(self):
        os.remove(filename)
    def test_append_to_file_one_line(self):
        #append current time to file 
        data = str(time.time())
        self.f.append_to_file(data)
        
        with open(filename, 'r') as testfile:
            all_lines = testfile.readlines()
        
        self.assertEqual(data, all_lines[len(all_lines)-1])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()