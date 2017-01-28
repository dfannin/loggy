""" library for counting contest multipler ( band mode qth )

input is intermediate file format
counts unique band, mode, qth entries 
returns multipler

example use:

multi = Mutipler_BMQ()

for qso in adif:
    multi.addrow(qso)
   
print multi.mutlipler()


Author" David Fannin
Copyright" 2017, David Fannin
License: See Project License File

"""

class Multipler_BMQ(object):
    def __init__(self):
        self.multi = {}

    def addrow(self,row):
        band =  row['band'].replace("M","") 
        mode = row['mode']
        if ( mode == 'SSB' ):
            mode = 'PH'
        comment = row['comment'].split(',') 
        qth = comment[2].upper()
        bandmodeqth = band + " " +  mode + " " + qth

        if not bandmodeqth  in self.multi:
            self.multi[bandmodeqth] = 1
        else:
            self.multi[bandmodeqth] += 1

    def multipler(self):
        return len(self.multi)

    def dump(self):
        return [ self.multi ]
