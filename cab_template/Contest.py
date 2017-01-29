

class Contest(object):

    def __init__(self,mycall):
        self.name = "Generic"
        self.description = "Generic Contest"
        self.qso = {}
        self.mycall = mycall 
        self._qsocount = 0 
        self.multilist = {}


    def _transform(self,row):
        return row

    def addrow(self, row):
        self.qso = self._transform(row)
        self._checkmulti()
        self._checkstats()

    def _checkmulti(self):
        band = self.qso['band']
        mode = self.qso['mode']
        bandmode = band + " " + mode
        if not bandmode in self.multilist:
            self.multilist[bandmode] = 1
        else:
            self.multilist[bandmode] += 1


    def _checkstats(self):
        self._qsocount += 1

    def multipler(self):
        return len(self.multilist) 

    def multipler_dump(self):
        return self.multilist

    def dups(self):
        return 0

    def qsocount(self):
        return self._qsocount 

    def format_cabrillo_row(self):
        freq =  int( float(self.qso['freq']) * 1000.0 )
        mode = self.qso['mode']
        qso_date = self.qso['qso_date']
        qso_date = qso_date[:4] + '-' + qso_date[4:6] + '-' + qso_date[6:]
        return 'QSO: %s %s %s %s %s %s 59' % (freq, mode, qso_date, self.qso['time_on'], self.mycall.upper(), self.qso['call'])

