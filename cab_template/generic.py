""" helper function to process adif row to Cabrillo format Generic

Author" David Fannin
Copyright" 2017, David Fannin
License: See Project License File

"""
def cab_template_generic(row,mycall):
    band =  row['band'].replace("M","") 
    freq =  int( float(row['freq']) * 1000.0 )
    mode = row['mode']
    qso_date = row['qso_date'] 
    qso_date = qso_date[:4] + '-' + qso_date[4:6] + '-' + qso_date[6:] 
    return 'QSO: %s %s %s %-8s %-8s %-8s' % (freq, mode, qso_date,row['time_on'] , mycall.upper(), row['call']) 
