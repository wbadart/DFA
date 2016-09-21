#!/usr/bin/env python

'''
' main.py
'
' Driver program to execute demonstration
' of DFA class.
'
' Will Badart
' SEP 2016
'
'''

import sys
import getopt
from os import path
from dfa import DFA


#================
# Default values
#================

INTERACTIVE = False
MACHINE_DEF = 'M1.txt'
TEST_STRS   = 'M1-Accept.txt'


#===================
# Utility functions
#===================

def usage():
    print >>sys.stderr, '''usage: {} [ -m FNAME -s FNAME -i -h ]
    -m FNAME    read in machine definition from FNAME
    -s FNAME    read in test strings from FNAME
    -i          enable interactive mode
    -h          disaply this help text'''.format(sys.argv[0])
    sys.exit(0)

def error(msg):
    print >>sts.stderr, str(msg)
    sys.exit(1)


#============================
# Parse command-line options
#============================

try:
    opts, args = getopt.getopt(sys.argv[1:], 'm:s:ih')
except getopt.GetoptError as err:
    error(err)

for o, a in opts:
    if o == '-h':
        usage()
    elif o == '-i':
        INTERACTIVE = True
    elif o == '-m':
        if path.isfile(a):
            MACHINE_DEF = a
        else:
            error('No such file, "{}"'.format(a))
    elif o == '-s':
        if path.isfile(a):
            TEST_STRS = a
        else:
            error('No such file, "{}"'.format(a))


#================
# Run simulation
#================

uut = DFA(MACHINE_DEF)

if INTERACTIVE:
    uut.step()
else:
    uut.test(TEST_STRS)
