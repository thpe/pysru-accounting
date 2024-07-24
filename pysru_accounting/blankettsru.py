import re
import numpy as np
import pandas as pd
from datetime import datetime


class BlankettSRU:
    def __init__(self):
        print('init')
        self.lines = []
        self.upp   = []
        self.blktt = ''
        self.prog = 'PySRU'

    def blankett(self, v):
        self.blktt = v

    def orgnr (self, org):
        self.org = org
        self.id = self.org + datetime.today().strftime(' %Y%m%d %H%M%S')

    def id(self, nr):
        self.id = nr

    def name(self, name):
        self.name = name

    def uppgift(self, u):
        self.upp.append(u)

    def uppgift_num(self, sru, val):
        self.upp.append(str(sru) + ' ' + str(int(val)))

    def print(self):
        print(self.generate())

    def generate(self):
        content = ''.join(['#BLANKETT ',   self.blktt, '\n',
                           '#IDENTITET ',  self.id,       '\n',
                           '#SYSTEMINFO ', self.prog,     '\n'])
        for u in self.upp:
            content = content + '#UPPGIFT ' + u + '\n'
        content = content + '#BLANKETTSLUT' + '\n'
        content = content + '#FIL_SLUT'
        return content

    def write(self, filename):
        content = self.generate().encode('iso-8859-1')
        with open(filename, 'wb') as f:
            f.write (content)
