"""
Docstring
"""

import os

class FileHandler():

    def __init__(self, PATH_LIST: list):
        self.PATH_LIST = PATH_LIST

    def greet(self):
        print(f"Hello {self.PATH_LIST[0]}")

