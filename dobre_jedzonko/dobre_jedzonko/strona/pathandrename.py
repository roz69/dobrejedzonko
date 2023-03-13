from uuid import uuid4
import os

class PathAndRename:
    def __init__(self, path):
        self.path = path

    def wrapper(self, instance, filename):
        ext = filename.rsplit('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        
        return os.path.join(self.path, filename)