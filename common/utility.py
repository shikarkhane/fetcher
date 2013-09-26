'''
Created on Sep 26, 2013

@author: nikhil
'''

class File_handler():
    '''
    anything related to file writing/deleting etc
    '''
    def __init__(self, file_path):
        self.file_path = file_path
    def append_to_file(self, data):
        with open(self.file_path, 'a') as f:
            f.write(data)

            