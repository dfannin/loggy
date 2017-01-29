
from . import Contest

class NAQP(Contest.Contest):

    def __init__(self,mycall,myname,myqth):
        super(NAQP, self).__init__(mycall)
        self.name = "NAQP"
        self.description = "North American QSO Party"
        #self.qso = {}
        # self.mycall = mycall 
        self.myname = myname
        self.myqth = myqth
        #self._qsocount = 0 
        #self.multilist = {}


    def _checkmulti(self):
        band = self.qso['band']
        mode = self.qso['mode']
        comment = self.qso['comment'].split(',')
        qth = comment[2].upper()
        bandmodeqth = band + " " + mode + " " + qth
        if not bandmodeqth in self.multilist:
            self.multilist[bandmodeqth] = 1
        else:
            self.multilist[bandmodeqth] += 1

    def format_cabrillo_row(self):
        freq =  int( float(self.qso['freq']) * 1000.0 )
        mode = self.qso['mode']
        if ( mode == 'SSB' ):
            mode = 'PH'
        qso_date = self.qso['qso_date']
        qso_date = qso_date[:4] + '-' + qso_date[4:6] + '-' + qso_date[6:]
        comment = self.qso['comment'].split(',')
        name = comment[1].upper()
        qth = comment[2].upper()
        return 'QSO: %s %s %s %s %s %s %s %-8s %-12s %-4s' % (freq, mode, qso_date, self.qso['time_on'] , self.mycall.upper(), self.myname.upper(), self.myqth.upper(), self.qso['call'], name, qth)
