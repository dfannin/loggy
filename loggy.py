#!/usr/bin/env python3 


import sys
import getopt
from  lib import *
from  cab_template import *

import pprint

def main():

    mycall = 'KK6DF'
    myqth  = 'CA'
    myname  = 'DAVE'
    cab_temp = naqp.cab_template_naqp


    myadi  = ADIF.ADIF(fn)

    stat = Stats.Stats()
    multi = Multipler_BMQ.Multipler_BMQ()


    for i in iter(myadi):
        stat.addrow(i)
        multi.addrow(i)
        print (cab_temp(i,mycall,myname,myqth) )
                

    print ( "\n\nStatistics:")
    pprint.pprint(stat.dump())

    print ("\n\nMultipliers:")
    print ( multi.multipler())
    pprint.pprint(multi.dump())

    score =  multi.multipler() * stat.qso() 
    print ( "score : %s" % ( score )) 


if __name__ == "__main__":

    fn = sys.argv[1]
    main()
