

class Experiment:
    def __init__(self, setup, date, mouse):
        super().__init__()
        self.setup = setup
        self.date = date
        self.mouse = mouse

    def __str__(self):
        return f"{self.mouse} used in {self.setup} experiment on {self.date}"

    # define the call function that is used to call the object as a function
    def __call__(self, setup, date, mouse):
        self.setup = setup
        self.date = date
        self.mouse = mouse


E1 = Experiment("Burrow", 230822, "EM0421")
E2 = Experiment("PPI", 230901, "EM0422")
E3 = Experiment("Burrow", 230822, "EM0423")

print(E1)
E1("Burrow", 230827, "EM0421")
print(E1)
