'''
Created on Sep 26, 2013

@author: nikhil
'''
import json
import datetime
from gdal_country import Point, CountryChecker
import settings
class Coordinate_handler():
    def find_country_code_for_coordinates(self, coord):
        cc = CountryChecker(settings.RESOURCE_PATH + "/" + settings.GDAL_SHAPE_FILENAME)
        # twitter coord are switched
        try:
            cc_code = cc.getCountry(Point(coord[1], coord[0])).iso
        except Exception, e:
            print coord, str(e)
            cc_code = "error"
        return cc_code
    def skip_this_data(self, data, accepting_country_codes):
        coord = data.get("coordinates").get("coordinates") 
        if self.find_country_code_for_coordinates(coord) in accepting_country_codes:
            return False
        else:
            return True
class File_handler():
    '''
    anything related to file writing/deleting etc
    '''
    def __init__(self, file_path):
        self.file_path = file_path
    def append_to_file_as_json(self, data):
        with open(self.file_path, 'a') as f:
                json.dump(data, f) 
                f.write("\n")
class Date_handler():
    """all dates should be in utc"""
    def get_current_utc_date_string(self, format):
        now = datetime.datetime.now()
        return now.strftime(format)