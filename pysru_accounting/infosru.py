import re
import numpy as np
import pandas as pd


class InfoSRU:
    def __init__(self):
        print('init')
        self.lines = []

    def filename(self, name):
        self.filename = name

    def organisation_nr(self, nr):
        self.orgnr = nr

    def name(self, name):
        self.name = name

    def postcode(self, postcode):
        self.postcode = postcode

    def town(self, town):
        self.town = town

    def print(self):
        print('#DATABESKRIVNING_START')
        print('#PRODUKT SRU')
        print('#PROGRAM pysru-accounting')
        print('#FILNAMN ' + self.filename)
        print('#DATABESKRIVNING_SLUT')
        print('#MEDIELEV_START')
        print('#ORGNR '   + self.orgnr)
        print('#NAMN '    + self.name)
        print('#POSTNR '  + self.postcode)
        print('#POSTORT ' + self.town)
        print('#MEDIELEV_SLUT')
