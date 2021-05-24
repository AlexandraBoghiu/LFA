import re

f = open('your_config_file', mode="r")
linii = f.readlines()


def validareStari(string):
    if ',' in string:
        stare = string.strip().split(",", maxsplit=1)[0]
        tip = ''.join(string.strip().split(",", maxsplit=1)[1].split())
        return (stare, tip)
    else:
        stare = string.strip()
        tip = "0"
        return (stare, tip)


class ValidationException(Exception):
   pass


class Automaton():
    words = []
    stari = set()
    alfabet = set()
    sectiuniCitite = [0, 0, 0]  # sigma, states, transitions
    sectiuneCurenta = 0
    stareInitiala = 0
    stariFinale = set()
    tranzitii = []
    valid = True
    ok = 0
    ok2 = 0
    ok3 = 0
    lista = []
    verif = 1

    def __init__(self, config_file):
        self.config_file = config_file
      #  print("Hi, I'm an automaton!")

    def validate(self):
        for i in range(len(linii)):
            if re.search('#+', linii[i].strip()) == None and re.search('.', linii[i]) != None:
                if "".join(linii[i].split()) == "Sigma:":
                    if self.sectiuniCitite[0] == 1 or self.sectiuneCurenta == 1:
                        print("invalid")
                        raise ValidationException("The config file is invalid.")
                    else:
                        self.sectiuneCurenta = 1
                        self.sectiuniCitite[0] = 1
                elif "".join(linii[i].split()) == "States:":
                    if self.sectiuneCurenta == 0 and self.sectiuniCitite[1] == 0:
                        self.sectiuneCurenta = 2
                        self.sectiuniCitite[1] = 1
                    elif self.sectiuneCurenta == 2 or self.sectiuniCitite[1] == 1:
                        print("invalid")
                        raise ValidationException("The config file is invalid.")
                elif "".join(linii[i].split()) == "Transitions:":
                    if self.sectiuneCurenta == 0 and self.sectiuniCitite[2] == 0:
                        self.sectiuneCurenta = 3
                        self.sectiuniCitite[2] = 1
                    else:
                        print("invalid")
                        raise ValidationException("The config file is invalid.")
                elif linii[i].strip() == "End":
                    if self.sectiuneCurenta != 0:
                        self.sectiuneCurenta = 0
                    else:
                        print("invalid")
                        raise ValidationException("The config file is invalid.")  # end nu corespunde

                if self.sectiuneCurenta == 1:
                    if len("".join(linii[i].strip())) >= 1:
                        if ("".join(linii[i].strip()) not in self.alfabet and " " not in "".join(linii[i].strip())):
                            self.alfabet.add(linii[i].strip())
                        elif "".join(linii[i].strip()) in self.alfabet:
                            print("invalid")
                            raise ValidationException("The config file is invalid.")
                        else:
                            print("invalid")
                            raise ValidationException("The config file is invalid.")  # nu poate exista spatiu in simbol

                if self.sectiuneCurenta == 2:
                    self.perecheStari = validareStari(linii[i])
                    self.stari.add(self.perecheStari[0])
                    if (self.perecheStari[1] == 'S'):
                        if self.stareInitiala != 0:  # prea multe stari initiale
                            print("invalid")
                            raise ValidationException("The config file is invalid.")
                        else:
                            self.stareInitiala = self.perecheStari[0]
                    if (self.perecheStari[1] == 'F'):
                        self.stariFinale.add(self.perecheStari[0])
                    if (self.perecheStari[1] == "FS" or self.perecheStari[1] == "SF"):
                        if self.stareInitiala != 0:
                            print("invalid")
                            raise ValidationException("The config file is invalid.")  # prea multe stari initiale

                if self.sectiuneCurenta == 3:
                    self.tranzitii.append(re.findall("\w+", linii[i]))

                if len(self.tranzitii) > 0 and self.ok == 0:
                    self.tranzitii.remove(self.tranzitii[0])
                    self.ok = 1
                if len(self.stari) > 0 and self.ok2 == 0:
                    self.stari.remove('States:')
                    self.ok2 = 1
                if len(self.alfabet) > 0 and self.ok3 == 0:
                    self.alfabet.remove('Sigma:')
                    self.ok3 = 1

        verifStari = [stare for stare in self.stari]
        verifAlfabet = [simbol for simbol in self.alfabet]
        verifStari = sorted(verifStari)
        verifAlfabet = sorted(verifAlfabet)
        verifTranz = [[0 for i in verifAlfabet] for j in verifStari]
        for tranzitie in self.tranzitii:
            if len(tranzitie) != 3:
                print("invalid")
                raise ValidationException("The config file is invalid.")
            elif tranzitie[0] not in self.stari or tranzitie[1] not in self.alfabet or tranzitie[2] not in self.stari:
                print("invalid")
                raise ValidationException("The config file is invalid.")
            elif verifTranz[verifStari.index(tranzitie[0])][verifAlfabet.index(tranzitie[1])] == 1:
                print("invalid")
                raise ValidationException("The config file is invalid.")
            verifTranz[verifStari.index(tranzitie[0])][verifAlfabet.index(tranzitie[1])] = 1

        return self.valid


    def accepts_input(self, input_str):
        pass

    def read_input(self, input_str):
        pass

if __name__ == "__main__":
    a = Automaton('your_config_file')
    print(a.validate())
