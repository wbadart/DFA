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

class DFA:

    #====================================================
    # Construct DFA model based on rules listed in FNAME
    #====================================================

    def __init__(self, fname):

        fs = open(fname)
        self.d = dict();

        for i, line in enumerate(fs.readlines()):

            line = line.rstrip()

            # line 1 is metadata about the machine
            if i == 0:
                self.name = line

            # the next line is the alphabet, sigma
            elif i == 1:
                self.E = line.split(',')

            # line 3 is the set of states
            elif i == 2:
                self.Q = line.split(',')

            # line 4 holds the initial state
            elif i == 3:
                self.q0 = line

            # line 5 lists the accepting states
            elif i == 4:
                self.F = line.split(',')

            # the remaining lines hold the transition rules
            else:
                transition = line.split(',')
                print 'Rule #{}: {}'.format(len(self.d) + 1, line.rstrip())
                self.d[(transition[0], transition[1])] = transition[2]

        self.current_state = self.q0
        fs.close()


    #==================================================
    # Update self.current_state based on an input char
    #==================================================

    def transition(self, char):
        if (self.current_state, char) not in self.d:
            return False
        self.current_state = self.d[(self.current_state, char)]
        return True


    #===============================================
    # Run the simulation on one input string (line)
    #===============================================

    def run(self, line):

        line = line.rstrip()
        print 'Machine "{}" processing string "{}"'.format(self.name, line)
        print ', '.join(self.E)

        for i, char in enumerate(line):

            # Sanity checks
            if char not in self.E:
                print 'Character "{}" not in alphabet.'.format(char)
                break
            if (self.current_state, char) not in self.d:
                print 'No rule for ({}, {}).'.format(self.current_state, char)
                break

            # Follow transition rule
            next_state = self.d[(self.current_state, char)]
            print 'Step #{}: ({}, {}) -> {}'.format(i + i, self.current_state, char, next_state)
            self.transition(char)

        print 'Accepted' if self.current_state in self.F else 'Rejected'
        print


    #==============================================
    # Run the simulation on a file of test strings
    #==============================================

    def test(self, fname):
        fs = open(fname)
        for line in fs.readlines():
            self.run(line)
        fs.close()


    #================================================================
    # Step through the simulation, inputting one character at a time
    #================================================================

    def step(self):
        print 'Initial state: {}'.format(self.q0)
        str_in = raw_input('> ')
        while True:
            self.transition(str_in.rstrip())
            print 'State: {}, {}'.format(\
                    self.current_state, 'accepted' if self.current_state in self.F else 'rejected')
            str_in = raw_input('> ')
            if str_in == 'Q':
                break
