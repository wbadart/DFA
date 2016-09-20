'''
' dfa.py
'
' Class definition of representation of a DFA
' based on an instruction file and then produces
' an output based on the way the target DFA would
' process an input string.
'
' Will Badart
' SEP 2016
'
'''

import fileinput

class DFA:
    def __init__(self):
        for i, line in enumerate(fileinput.input()):
            if i == 1:
                continue
            if i == 2:
                self.E = line.split(', ');
