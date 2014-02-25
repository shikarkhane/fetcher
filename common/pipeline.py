import settings

class Pipe():
    '''Pipe sort of a cache system. We will store IDs of incoming data and make sure that we dont pass on duplicates.
    For eg. twitter stream might send us duplicate data. By checking if the ID exists in the pipe, we will avoid
    dirty data issue for a short time
    Size of a pipe is not meant to be very large cause we dont want to create memory hog and we dont expect the data
    providers like twitter or instagram to have a duplicates problem after say 1000 posts'''
    def __init__(self):
        self.size = settings.PIPELINE_SIZE
        self.pipe = []
    def maintain(self):
        if len(self.pipe) > self.size:
            self.pipe.pop(0)
    def add(self, new_id):
        new_id = str(new_id)
        result = False
        if new_id in self.pipe:
            result = False
        else:
            self.pipe.append(new_id)
            result = True
        self.maintain()
        return result


