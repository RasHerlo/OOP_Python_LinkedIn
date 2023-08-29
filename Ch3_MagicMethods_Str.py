

class Experiment:
    def __init__(self, setup, date, mouse):
        super().__init__()
        self.setup = setup
        self.date = date
        self.mouse = mouse
        self._delay = 5

    def __str__(self):
        return f"{self.mouse} used in {self.setup} experiment on {self.date}"

    def __repr__(self):
        return f"mouse={self.mouse}, setup={self.setup}, date={self.date}"

    def __eq__(self, value):
        if not isinstance(value, Experiment):
            raise ValueError("Can't compare Exp to non-Exp")
        return (self.mouse == value.mouse and
                self.setup == value.setup and
                self.date == value.date)

    def __ge__(self, value):
        if not isinstance(value, Experiment):
            raise ValueError("Can't compare Exp to non-Exp")
        return self.date >= value.date

    def __lt__(self, value):
        if not isinstance(value, Experiment):
            raise ValueError("Can't compare Exp to non-Exp")
        return self.date < value.date

    # Actually part of MagicAttr
    def __getattribute__(self, name):
        if name == "date":
            d = super().__getattribute__("date")
            dl = super().__getattribute__("_delay")
            return d + dl
        return super().__getattribute__(name)


E1 = Experiment("Burrow", 230822, "EM0421")
E2 = Experiment("PPI", 230901, "EM0422")
E3 = Experiment("Burrow", 230822, "EM0423")

print(str(E1))
print(repr(E2))

print(E1 == E3)
print(E1 == E2)
# print(E1 == 1)

exps = [E3, E2, E1]

exps.sort()
print([exp.mouse for exp in exps])

print(E3)
