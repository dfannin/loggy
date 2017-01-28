""" library to calculate statistics and counts from intermediate file 

Author" David Fannin
Copyright" 2017, David Fannin
License: See Project License File

"""
class Stats(object):
    def __init__(self):
        self.total = 0 
        self.mode = {}
        self.band = {}
        self.bandmode = {}

    def addrow(self,row):
        self.total += 1

        if not row['mode'] in self.mode:
            self.mode[row['mode']] = 1
        else:
            self.mode[row['mode']] += 1

        if not row['band'] in self.band:
            self.band[row['band']] = 1
        else:
            self.band[row['band']] += 1

        bandmode = row['band'] + ' ' + row['mode']

        if not bandmode  in self.bandmode:
            self.bandmode[bandmode] = 1
        else:
            self.bandmode[bandmode] += 1
    def qso(self):
        return self.total

    def dump(self):
        return [ self.total, self.mode, self.band, self.bandmode ]
