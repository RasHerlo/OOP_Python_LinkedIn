
# An interface is a contract to provide a certain kind of behaviour
# or capability

# Making the object capable of presenting themselves as json

# but instead of writing that in every time, you cna make an abstract-base
# class and just them inherit that
# see JSONify


# Abstract Base Classes
from abc import ABC, abstractmethod


# declaring that a class has 
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


# Building a drawing program

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14*(self.radius**2)

    def toJSON(self):
        return f"{{\"circle\" : {str(self.calcArea())} }}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
