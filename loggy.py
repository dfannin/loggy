#!/usr/bin/env python3 


import sys
import getopt
import configparser

from  lib import *
from  cab_template import *

import pprint

def main():



    myadi  = ADIF.ADIF(afn)

    stat = Stats.Stats()

    if contest == "GENERIC":
    	multi = Multipler_BM.Multipler_BM()
    if contest == "NAQP":
    	multi = Multipler_BMQ.Multipler_BMQ()


    for i in iter(myadi):
        stat.addrow(i)
        multi.addrow(i)
        if contest == "GENERIC":
        	print (cab_temp(i,mycall) )
        if contest == "NAQP":
        	print (cab_temp(i,mycall,myname,myqth) )
                

    print ( "\n\nStatistics:")
    pprint.pprint(stat.dump())

    print ("\n\nMultipliers:")
    print ( multi.multipler())
    pprint.pprint(multi.dump())

    score =  multi.multipler() * stat.qso() 
    print ( "score : %s" % ( score )) 


if __name__ == "__main__":

    cfn = "config.ini"

    config = configparser.ConfigParser()
    config.read_file(open(cfn))

    mycall = config['default']['call']
    myname  = config['default']['name']
    myqth  = config['contest']['qth']
    contest = config['contest']['contest']
    afn  = config['file']['adif']
    ofn  = config['file']['output']

    if contest == 'NAQP':
    	cab_temp = naqp.cab_template_naqp

    if contest == 'GENERIC':
    	cab_temp = generic.cab_template_generic

    if len(sys.argv) > 1:
    	afn = sys.argv[1]

    main()
