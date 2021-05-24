import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

f = open('your_config_file', mode="r")
linii = f.readlines()

from automaton.automaton import Automaton

class RejectionException(Exception):
    pass

class DFA(Automaton):

    def __init__(self, config_file):
        super().__init__(config_file)
        # print("More precisely, a DFA.")
        self.validate()

    def validate(self):
        return super().validate()


    def accepts_input(self, input_str):
        stareActuala = self.stareInitiala
        gasit = False
        nr = 0
        for litera in input_str:
            gasit = False
            for t in self.tranzitii:
                if (t[0] == stareActuala and litera == t[1]):
                    stareActuala = t[2]
                    gasit = True
                    nr += 1
                    break
            if gasit == False:
                break
        if (nr != len(input_str)):
            raise RejectionException()
        else:
            return self.read_input(stareActuala)

    def read_input(self, input_str):
        if input_str in self.stariFinale:
            return True
        return False


if __name__ == "__main__":
    num_args = len(sys.argv)
   # if num_args > 1:
      #  print(f"I see you provided {num_args - 1} argument{'s' if num_args > 2 else ''} from the console.")
      #  print("Here's a list with all the system arguments:")
      #  for i, arg in enumerate(sys.argv):
       #     print(f"Argument {i}: {arg:>32}")
       # print()

    dfa = DFA('your_config_file')
    if dfa.accepts_input(sys.argv[3]) == True:
        print("accept")
    else:
        print("reject")
