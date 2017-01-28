""" helper function to process adif row to Cabrillo format NA Qso Party

Author" David Fannin
Copyright" 2017, David Fannin
License: See Project License File

"""
def cab_template_naqp(row,mycall,myname,myqth):
    band =  row['band'].replace("M","") 
    freq =  int( float(row['freq']) * 1000.0 )
    mode = row['mode']
    if ( mode == 'SSB' ):
        mode = 'PH'
    qso_date = row['qso_date'] 
    qso_date = qso_date[:4] + '-' + qso_date[4:6] + '-' + qso_date[6:] 
    comment = row['comment'].split(',') 
    name = comment[1].upper()
    qth = comment[2].upper()
    return 'QSO: %s %s %s %s %s %s %s %-8s %-12s %-4s' % (freq, mode, qso_date,row['time_on'] , mycall.upper(), myname.upper(), myqth.upper(), row['call'], name, qth) 
