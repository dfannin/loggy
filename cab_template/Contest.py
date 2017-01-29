import collections

class Contest(object):

    def __init__(self,config):
        self.config = config
        self.name = "GENERIC"
        self.description = "Generic Contest"
        self.qso = {}
        self._qsocount = 0 
        self.multilist = {}
        self.tags = collections.OrderedDict()
        self.set_cabrillo_tags()

    def set_cabrillo_tags(self):
        self.tags = collections.OrderedDict([
                ('CALLSIGN', self.config['default']['call']),
                ('CONTEST', self.config['contest']['contest']),
                ])
        for tag in self.config['cabrillo']:
            self.tags[tag] = self.config['cabrillo'][tag]

    def _transform(self,row):
        return row

    def addrow(self, row):
        self.qso = self._transform(row)
        if not self.qso:
            return
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
        return 'QSO: %s %s %s %s %s %s 59' % (freq, mode, qso_date, self.qso['time_on'], self.config['default']['call'].upper(), self.qso['call'])

    def cabrillo_header(self):
        hdr = "START-OF-LOG: 3.0\n"
        for tag,tagval  in self.tags.items():
            # if multiline string, then split and add tag to each line
            if tagval.count("\n") > 0:
                for line in tagval.split('\n'):
                    hdr += tag.upper() + ": " + line + "\n" 
            else:
                hdr +=  tag.upper() + ": " + tagval + "\n"
        return hdr

    def cabrillo_footer(self):
        ftr = "END-OF-LOG:\n"
        return ftr
