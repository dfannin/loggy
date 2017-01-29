
from . import Contest

class NAQP_SSB(Contest.Contest):

    def __init__(self,config):
        super(NAQP_SSB, self).__init__(config)
        self.name = "NAQP-SSB"
        self.description = "North American QSO Party - Single Side Band"

    def _transform(self,row):
        if row['mode'] == "SSB":
            return row
        else:
            return []

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
        if not self.qso:
            return ''
        freq =  int( float(self.qso['freq']) * 1000.0 )
        mode = self.qso['mode']
        if ( mode == 'SSB' ):
            mode = 'PH'
        qso_date = self.qso['qso_date']
        qso_date = qso_date[:4] + '-' + qso_date[4:6] + '-' + qso_date[6:]
        comment = self.qso['comment'].split(',')
        name = comment[1].upper()
        qth = comment[2].upper()
        return 'QSO: %5s %2s %s %s %-15s %-10s %-3s %-15s %-10s %-3s' % (freq, mode, qso_date, self.qso['time_on'] , self.config['default']['call'].upper(), self.config['contest']['name'].upper(), self.config['contest']['qth'].upper(), self.qso['call'], name, qth)

class NAQP_CW(Contest.Contest):

    def __init__(self,config):
        super(NAQP_CW, self).__init__(config)
        self.name = "NAQP-CW"
        self.description = "North American QSO Party - Continuous Wave"

    def _transform(self,row):
        if row['mode'] == "CW":
            return row
        else:
            return []

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
        if not self.qso:
            return ''
        freq =  int( float(self.qso['freq']) * 1000.0 )
        mode = self.qso['mode']
        if ( mode == 'SSB' ):
            mode = 'PH'
        qso_date = self.qso['qso_date']
        qso_date = qso_date[:4] + '-' + qso_date[4:6] + '-' + qso_date[6:]
        comment = self.qso['comment'].split(',')
        name = comment[1].upper()
        qth = comment[2].upper()
        return 'QSO: %5s %2s %s %s %-15s %-10s %-3s %-15s %-10s %-3s' % (freq, mode, qso_date, self.qso['time_on'] , self.config['default']['call'].upper(), self.config['contest']['name'].upper(), self.config['contest']['qth'].upper(), self.qso['call'], name, qth)
