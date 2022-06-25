
import os

class fileHandler:
    def __init__(self):
        return


    def load_file_str(self,fn):
        return open(fn,"r").read()

    def load_file_arr(self,fn):
        return open(fn,"r").read().split('\n')


    