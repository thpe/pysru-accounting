import re
import numpy as np
import pandas as pd

class BlankettSRU:
    def __init__ (self):
        print ('init')
        self.lines = []

    def info (self, info):
        self.info = info

    def id (self, nr):
        self.id = nr

    def name (self, name):
        self.name = name

    def uppgift (self, u):
        self.upp.append(u)

    def print (self):
        print ('#BLANKETT '+self.blankett)
        print ('#IDENTITET '+self.id)
        print ('#SYSTEMINFO '+self.info)
        for upp in self.uppgift:
            print ('#UPPGIFT '+upp)
        print ('#POSTNR '+self.postcode)
        print ('#BLANKETTSLUT')
        print ('#FIL_SLUT')
