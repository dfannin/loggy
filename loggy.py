#!/usr/bin/env python3 
""" 

name: loggy.py

description: 
main program for adif to cabrillo log file processing, transformation and analaytics program

usage: 

    usually, just run "loggy.py"
    see "config.ini" file for many options, including input and output file names

Author: David Fannin
Copyright: 2017, David Fannin
License: New BSD (3 clause)
Python Version: 3

"""

import sys
import getopt
import configparser

from  lib import *
from  contest import *

import pprint


loggy_version = "1.0.a"

def main():

    input_type = config['file']['input_type'] 
    cf = config['file']

    if input_type == "ADIF":
    	infile   = ADIF.ADIF(cf['adif'])
    elif input_type == "CSV":
        # need to parse the field string into a list (and strip spaces)
    	infile   = CSV.CSV( cf['csv'], [x.strip() for x in cf['csv_fields'].split(",")])
    elif input_type == "MYSQL":
    	infile   = MYSQL.MYSQL( cf['myqsl_qry'], cf['mysql_connector'] )
    
    if config['contest']['contest'] == "GENERIC":
        mycontest = Contest.Contest(config) 

    if config['contest']['contest'] == "NAQP-SSB":
        mycontest = Contest_NAQP.NAQP_SSB(config)

    if config['contest']['contest'] == "NAQP-CW":
        mycontest = Contest_NAQP.NAQP_CW(config)
                
    print(mycontest.description) 

    cabrillo_qsos = ''
    for i in iter(infile):
        mycontest.addrow(i)
        cabrillo_qsos += mycontest.format_cabrillo_row() + "\n"

    cabrillo_qsos = cabrillo_qsos[:-1]

    print(mycontest.cabrillo_header())
    print(cabrillo_qsos) 
    print(mycontest.cabrillo_footer())
                

    #print ( "\n\nStatistics:")
    #print (mycontest.qsocount())

    #print ("\n\nMultipliers:")
    #print ( mycontest.multipler()  ) 
    #pprint.pprint ( mycontest.multipler_dump()  ) 

    #score =  mycontest.multipler() * mycontest.qsocount() 
    #print ("\n\nTotal:")
    #print ( "Score : %s" % ( score )) 

def usage():
    print ("loggy.py [-h] [-v] [-C alt_config.ini] [-c contest_name]  [-o output_file]  [adif_input_file]")
    print ("version " + loggy_version )
    print ("-h : help")
    print ("-v : version")
    print ("-C <ini file> : specify config.ini file")
    print ("-c <contest name> : use this contest name for processing and scoring")
    print ("-o <output file> : output file")
    print ("see: http://github.com/dfannin/loggy")

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvc:C:o:")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    # defaults
    cfn = "config.ini"
    contest_name = ""
    ofn = ""

    # read any command line options
    for o,a in opts:
        if o == "-h":
            usage()
            sys.exit()
        if o == "-v":
            print(loggy_version) 
            sys.exit()
        elif o == "-C":
            cfn = a 
        elif o == "-c":
            contest_name = a
        elif o == "-o":
            ofn = a

    # read the config file
    config = configparser.ConfigParser()
    config.read_file(open(cfn))

    # override any config file entries from command line

    if ofn: 
        ofn  = config['file']['output']

    if contest_name:
        config['contest']['contest'] = contest_name

    try:
        a = args[0] 
        config['file']['adif'] = a
    except IndexError:
        pass

    main()
