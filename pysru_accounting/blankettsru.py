import re
import numpy as np
import pandas as pd
from datetime import datetime


class BlankettSRU:
    def __init__(self):
        self.lines = []
        self.upp   = []
        self.blktt = ''
        self.prog = 'PySRU'
        self.content = ''

        self.aname = ''
        self.org  = ''
        self.id   = ''

    def blankett(self, v):
        self.blktt = v

    def orgnr (self, org):
        self.org = org
        self.id = self.org + datetime.today().strftime(' %Y%m%d %H%M%S')

    def id(self, nr):
        self.id = nr

    def name(self, aname):
        self.aname = aname

    def clear_uppgift(self):
        self.upp = []

    def uppgift(self, u):
        self.upp.append(u)

    def uppgift_num(self, sru, val):
        self.upp.append(str(sru) + ' ' + str(int(val)))

    def print(self):
        print(self.content)

    def generate(self):
        self.content += f'#BLANKETT {self.blktt}\n'
        self.content += f'#IDENTITET {self.id}\n'
        self.content += f'#SYSTEMINFO {self.prog}\n'
        for u in self.upp:
            self.content = self.content + '#UPPGIFT ' + u + '\n'
        self.content = self.content + '#BLANKETTSLUT' + '\n'
        return self.content

    def finish_file(self):
        self.content = self.content + '#FIL_SLUT'
        return self.content

    def write(self, filename):
        self.content = self.finish_file().encode('iso-8859-1')
        with open(filename, 'wb') as f:
            f.write (self.content)
