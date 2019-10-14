from math import *

class FuncConverter:
    def __init__(self, *strings):
        self.strings = [x for i in strings]

    def __get__(self, index):
        return eval(self.strings[index])