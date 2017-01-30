""" 

name: ADIF.py

description:
library to read ADIF file, and return each row

reads any ADIF 1.0/2.0 file

returns each row as a dictionary, using fields as the key

uses an iterator interface


example use: 

# reads the adif file "filename" and outputs each qso as a dictionary
adif = ADIF(filename) 
for qso in adif:
    print(qso)

# reads another file
adif.setfilename(newfilename)
for qso in adif:
    print(qso)


Author: David Fannin
Copyright: 2017, David Fannin
License: See Project License File
Python Version: 3.0

"""

import re

class ADIF(object):
    """ Reads ADIF files (v1 or 2) and outputs a dictionary """
    def __init__(self,fn):
        self.fn = fn 
        self.adif_re = re.compile(r'<(.*?):(\d+).*?>([^<\t\f\v]+)')
        self._start()

    """ set a new file name to be read """
    def setfilename(self,fn):
        self.fn = fn 
        self._start()

    def _start(self):
        self.raw = re.split( '<eor>|<eoh>(?i)', open(self.fn).read() )
        self.raw.pop(0)
        self.raw.pop()

    """ iterator for adif class """
    def __iter__(self):
        return self

    def __next__(self):
       if not self.raw:
           raise StopIteration()
       qso = {}
       record = self.raw.pop()
       tags = self.adif_re.findall(record)
       for tag in tags:
          qso[tag[0].lower()] = tag[2][:int(tag[1])]
       return qso
