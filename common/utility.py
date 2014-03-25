'''
Created on Sep 26, 2013

@author: nikhil
'''
import json
import datetime
from gdal_country import Point, CountryChecker
import settings
from shutil import move
import shutil

class Coordinate_handler():
    def __init__(self):
        self.country_checker = CountryChecker(settings.RESOURCE_PATH + "/" + settings.GDAL_SHAPE_FILENAME)
    def find_country_code_for_coordinates(self, coord):
        # twitter coord are switched
        try:
            cc_code = self.country_checker.getCountry(Point(coord[1], coord[0])).iso
        except Exception, e:
            #print coord, str(e)
            cc_code = "error"
        return cc_code
    def skip_this_data(self, data, accepting_country_codes):
        # twitter coordinates are not always present even if its a geo-tagged, instead they have values in key "Places"
        # we will keep it simple right now and ignore anything which doesnt have get("coordinates").get("coordinates"). Later on we will make it more robust.
        try:
            coord = data.get("coordinates").get("coordinates")
        except:
            return True 
        if self.find_country_code_for_coordinates(coord) in accepting_country_codes:
            return False
        else:
            return True
    def reverse_lookup_locality(self, coord):
        #todo
        return 'Nearby!'
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
    def copy_file_to(self, source, dest):
        shutil.move(source, dest)

class Date_handler():
    """all dates should be in utc"""
    def get_current_utc_date_string(self, format):
        now = datetime.datetime.utcnow()
        return now.strftime(format)
    def get_utc_x_minutes_ago(self, x_in_minutes):
        return datetime.datetime.utcnow() - datetime.timedelta(minutes=x_in_minutes)