""" The PySRU blankett """
from datetime import datetime


class BlankettSRU:
    """ a SRU file with one, or more blanketts """
    def __init__(self):
        self.upp   = []
        self.blktt = ''
        self.prog  = 'PySRU'
        self.content = ''

        self.aname = ''
        self.org   = ''
        self._identity   = ''

    def blankett(self, blktt):
        """ set blankett field """
        self.blktt = blktt

    def orgnr (self, org):
        """ set organisation number """
        self.org = org
        self._identity = self.org + datetime.today().strftime(' %Y%m%d %H%M%S')

    def identity(self, number):
        """ set id """
        self._identity = number

    def name(self, aname):
        """ set author name """
        self.aname = aname

    def clear_uppgift(self):
        """ clear the data elements under uppgift """
        self.upp = []

    def uppgift(self, uppgift):
        """ add an uppgift """
        self.upp.append(uppgift)

    def uppgift_num(self, sru, val):
        """ add an uppgift """
        self.upp.append(str(sru) + ' ' + str(int(val)))

    def print(self):
        """ print the generated content """
        print(self.content)

    def generate(self):
        """ generate for the current blankett """
        self.content += f'#BLANKETT {self.blktt}\n'
        self.content += f'#IDENTITET {self._identity}\n'
        self.content += f'#SYSTEMINFO {self.prog}\n'
        for uppgift in self.upp:
            self.content = self.content + '#UPPGIFT ' + uppgift + '\n'
        self.content = self.content + '#BLANKETTSLUT' + '\n'
        return self.content

    def finish_file(self):
        """ finish the file for writing """
        self.content = self.content + '#FIL_SLUT'
        return self.content

    def write(self, filename):
        """ write the content to the file """
        self.content = self.finish_file().encode('iso-8859-1')
        with open(filename, 'wb') as file:
            file.write (self.content)
