""" writer for the info.sru file """


class InfoSRU:
    """ class for writing the file """
    def __init__(self):
        """ init """
        print('init')
        self.lines = []
        self._filename = ''
        self._town = ''
        self._postcode = ''
        self._name = ''
        self._orgnr = ''

    def filename(self, name):
        """ set the filename """
        self._filename = name

    def organisation_nr(self, orgnr):
        """ set organisation number """
        self._orgnr = orgnr

    def name(self, name):
        """ set author name """
        self._name = name

    def postcode(self, postcode):
        """ set postcode """
        self._postcode = postcode

    def town(self, town):
        """ set town """
        self._town = town

    def print(self):
        """ print the output """
        print (self.generate())

    def generate(self):
        """ generate the file content """
        string = ''.join([
                 '#DATABESKRIVNING_START'    , '\n',
                 '#PRODUKT SRU'              , '\n',
                 '#PROGRAM pysru-accounting' , '\n',
                 '#FILNAMN ' , self._filename , '\n',
                 '#DATABESKRIVNING_SLUT'     , '\n',
                 '#MEDIELEV_START'           , '\n',
                 '#ORGNR '   , self._orgnr   , '\n',
                 '#NAMN '    , self._name    , '\n',
                 '#POSTNR '  , self._postcode, '\n',
                 '#POSTORT ' , self._town    , '\n',
                 '#MEDIELEV_SLUT'            , '\n'])
        return string

    def write(self, filename):
        """ write the file """
        content = self.generate().encode('iso-8859-1')
        with open(filename, 'wb') as file:
            file.write (content)
