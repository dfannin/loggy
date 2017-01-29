#!/usr/bin/env python3 

import sys
import getopt
import configparser

from  lib import *
from  cab_template import *

import pprint

def main():



    myadi  = ADIF.ADIF(config['file']['adif'])


    
    if config['contest']['contest'] == "GENERIC":
        mycontest = Contest.Contest(config) 

    if config['contest']['contest'] == "NAQP-SSB":
        mycontest = Contest_NAQP.NAQP_SSB(config)

    if config['contest']['contest'] == "NAQP-CW":
        mycontest = Contest_NAQP.NAQP_CW(config)
                
    print(mycontest.description) 
    print(mycontest.cabrillo_header())

    for i in iter(myadi):
        mycontest.addrow(i)
        print(mycontest.format_cabrillo_row())

    print(mycontest.cabrillo_footer())
                

    print ( "\n\nStatistics:")
    print (mycontest.qsocount())

    print ("\n\nMultipliers:")
    print ( mycontest.multipler()  ) 
    pprint.pprint ( mycontest.multipler_dump()  ) 

    score =  mycontest.multipler() * mycontest.qsocount() 
    print ("\n\nTotal:")
    print ( "Score : %s" % ( score )) 


if __name__ == "__main__":

    cfn = "config.ini"

    config = configparser.ConfigParser()
    config.read_file(open(cfn))

    ofn  = config['file']['output']

    if len(sys.argv) > 1:
    	config['file']['adif'] = sys.argv[1]

    main()
