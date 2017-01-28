""" library for counting contest multipler ( band mode  )

input is intermediate file format
counts unique band, mode,  entries 
returns multipler

example use:

multi = Mutipler_BM()

for qso in adif:
    multi.addrow(qso)
   
print multi.mutlipler()


Author" David Fannin
Copyright" 2017, David Fannin
License: See Project License File

"""

class Multipler_BM(object):
    def __init__(self):
        self.multi = {}

    def addrow(self,row):
        band =  row['band'].replace("M","") 
        mode = row['mode']
        bandmode = band + " " +  mode 

        if not bandmode  in self.multi:
            self.multi[bandmode] = 1
        else:
            self.multi[bandmode] += 1

    def multipler(self):
        return len(self.multi)

    def dump(self):
        return [ self.multi ]
