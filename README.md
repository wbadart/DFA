Theory of Computing
===================

**Project01: DFA**

*Will Badart (netid: wbadart)*

This project aims to simulate a Deterministic Finite Automata (DFA) and to use that simulation to determine whether the machine under test accepts or rejects given strings. The core of the simulation is a class, "DFA," with a the following members and methods:

```
name: String; a label for the DFA
E:    List;   sigma, the alphabet of recongizable characters
Q:    List;   the set of states in which the machine can be
q0:   String; initial state
F:    List;   stores the accepting (final) states
d:    Dict;   {(String, Character), String} delta maps the tuple (current state, input character) to the next state

current_state: String; the name of the state the machine is currently in. Defaults to q0

None __init___(self, fname:String); constructor takes the name of the file which defines the unit under test

Bool transition(self, char:Character); updates self.current_state according to the input character. Returns False if transition failed

None run(self, line:String); test whether the machine accepts "line," delivers results through stdout

None test(self, fname:String); calls self.run on a list of test strings given in the file called "fname"

None step(self); interactively step though a test string one character at a time
```

## Quick start
Clone or download the repository and navigate to the downloaded/ extracted directory. Please ensure that you are using [Python 2.x](https://www.python.org/downloads/). Now simply run `./main.py -h` or refer to the example below for instructions on how to simulate your DFA.

**Example:**

```
$ git clone https://github.com/wbadart/DFA dfa && cd dfa
$ ./main.py -m M1.txt -s M1-Accept.txt
```

If for some reason `main.py` is not flagged as executable, you can flag it as such by running `chmod +x main.py`. Also, if Python 2 is not your default python binary, please run the program with `/path/to/python2/binary main.py [options]`.
