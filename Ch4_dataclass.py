
from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutableClass:
    val1: str = "value 1"
    val2: int = 0






@dataclass
class Experiment:
    setup: str = "No Setup provided"
    mouse: str = "No mouse registered"
    date: int = 0

    def __post_init__(self):
        self.description = f"{self.mouse} was used for {self.setup}" \
                           f" on {self.date}"


E1 = Experiment("Burrow", 230822, "EM0421")
E2 = Experiment("PPI", 230901, "EM0422")
E3 = Experiment("Burrow", 230822, "EM0421")

print(E1)
print(E1 == E3)

print(E1.description)

E4 = Experiment()
print(E4)
