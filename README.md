# LFA

EN: Project within the laboratory of Formal Languages and Automata theory, year 1, semester 2. The project was made in Python.

Exercise 1. Implement a library/program in a programming language of your
choosing to load and validate the following input file:
```
#
# comment lines ( skip them )
#
Sigma :
    word1
    word2
    ...
End
#
# comment lines ( skip them )
#
States :
    state1
    state2
    state3 ,F
    ...
    stateK , S
    ...
End
#
# comment lines ( skip them )
#
Transitions :
    stateX, wordY , stateZ
    stateX, wordY , stateZ
    ...
End
```

Sections can be in any order. By validation we ask to check that transition
section has valid states (first and third word) and valid words (word two). Note
that states can be succeeded by ”F”, ”S”, both or nothing. ”S” symbol can
succeed only one state.

Exercise 2:
Implement a library/program in a programming language of your
choosing that creates a DFA. Use your library from lab 1 to generate the DFA
based on input file. Then check of DFA accepts a give string. Allow command
line arguments to your program in the form:
```
your_dfa_engine.py  dfa_config_file  input_string
>> a c c e p t / r e j e c t
```
