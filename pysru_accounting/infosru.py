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
        print (self.generate())

    def generate(self):
        string = ''.join([
                 '#DATABESKRIVNING_START'    , '\n',
                 '#PRODUKT SRU'              , '\n',
                 '#PROGRAM pysru-accounting' , '\n',
                 '#FILNAMN ' , self.filename , '\n',
                 '#DATABESKRIVNING_SLUT'     , '\n',
                 '#MEDIELEV_START'           , '\n',
                 '#ORGNR '   , self.orgnr    , '\n',
                 '#NAMN '    , self.name     , '\n',
                 '#POSTNR '  , self.postcode , '\n',
                 '#POSTORT ' , self.town     , '\n',
                 '#MEDIELEV_SLUT'            , '\n'])
        return string

    def write(self, filename):
        content = self.generate().encode('iso-8859-1')
        with open(filename, 'wb') as f:
            f.write (content)
