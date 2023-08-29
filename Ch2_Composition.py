
# Building objects out of other object
# Object 1 HAS another object

# Fx: Experiment objects HAS mouse objects


# Experiment = (Mouse, Setup, Date)

# Mouse = (Name, Genotype, Age)

class Experiment:
    def __init__(self, setup, date, mouse=None):
        self.setup = setup
        self.date = date

        self.mouse = mouse

        self.paradigms = []

    def addparadigm(self, paradigm):
        self.paradigms.append(paradigm)

    def countparadigms(self):
        result = 0
        for p in self.paradigms:
            result += 1
        return result


class Mouse:
    def __init__(self, number, genotype, sex, born):
        self.number = number
        self.genotype = genotype
        self.sex = sex
        self.born = born

    def __str__(self):
        return f"{self.number} {self.genotype} {self.sex} {self.born}"


class Paradigm:
    def __init__(self, timestamp, stimuli):
        self.timestamp = timestamp
        self.stimuli = stimuli


M1 = Mouse("EM0420", "TIGRE/bPAC", "F", 220822)
E1 = Experiment("Burrow", 230829, M1)

E1.addparadigm(Paradigm([0, 999], "AP"))
E1.addparadigm(Paradigm([1000, 1999], "Chill"))
E1.addparadigm(Paradigm([2000, 2999], "AP"))

print(E1.mouse)
print(E1.setup)
print(E1.countparadigms())
