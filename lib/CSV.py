""" 

name: CSV.py

description:
library to read CSV file, and return each row


returns each row as a dictionary, using fields as the key

uses an iterator interface


example use: 

# reads the csv file "filename" and outputs each qso as a dictionary
csv = CSV(filename,fields) 
for qso in csv:
    print(qso)

# reads another file
csv.setfilename(newfilename)
for qso in csv:
    print(qso)


Author: David Fannin
Copyright: 2017, David Fannin
License: See Project License File
Python Version: 3.0

"""

import csv
import pprint

class CSV(object):
    """ Reads csv and outputs a dictionary """
    def __init__(self,fn, fdn):
        self.fn = fn 
        self.fdn = fdn 
        self._start()

    """ set a new file name to be read """
    def setfilename(self,fn):
        self.fn = fn 
        self._start()

    def _start(self):
        self.raw = csv.DictReader(open(self.fn),fieldnames=self.fdn) 

    """ iterator for csv class """
    def __iter__(self):
        return self

    def __next__(self):
       if not self.raw:
           raise StopIteration()
       qso = next(self.raw)
       qso = dict(qso)
       return qso
