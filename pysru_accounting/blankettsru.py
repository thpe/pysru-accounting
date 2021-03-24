import re
import numpy as np
import pandas as pd
from datetime import datetime


class BlankettSRU:
    def __init__(self):
        print('init')
        self.lines = []
        self.upp   = []
        self.blankett = ''
        self.postcode = ''

    def info(self, info):
        self.info = info

    def orgnr (self, org):
        self.org = org
        self.id = self.org + datetime.today().strftime(' %Y%m%d %H%M%S')

    def id(self, nr):
        self.id = nr

    def name(self, name):
        self.name = name

    def uppgift(self, u):
        self.upp.append(u)

    def print(self):
        print('#BLANKETT '   + self.blankett)
        print('#IDENTITET '  + self.id)
        print('#SYSTEMINFO ' + self.info)
        for u in self.upp:
            print('#UPPGIFT ' + u)
        print('#POSTNR ' + self.postcode)
        print('#BLANKETTSLUT')
        print('#FIL_SLUT')
