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
        print ("************using generic") 
        mycontest = Contest.Contest(config['default']['call']) 

    if config['contest']['contest'] == "NAQP":
        print ("************using naqp") 
        mycontest = Contest_NAQP.NAQP(config['default']['call'], config['default']['name'],config['contest']['qth'] )
                

    for i in iter(myadi):
        mycontest.addrow(i)
        print(mycontest.format_cabrillo_row())
                

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
