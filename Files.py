'''This class is for testing the oop file implementation'''

#version 1

import os
class File:
    def __init__(self):
        pass

    def getSize(self,path):
        if not os.path.isdir(path):
            return
        name_list = os.listdir(path)
        size = 0
        for files in name_list:
            pathIndex = f'{path}/{files}'
            if os.path.isdir(pathIndex):
                size += self.getSize(pathIndex)
            else:
                size += os.path.getsize(pathIndex)
        return size






