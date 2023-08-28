
class Raster:
    # Properties defined at the class level shared by all instances
    # Class-attributes
    EXP_TYPES = ('Burrow', 'PPI')

    # double-underscore generates secret private variable
    __experimentlist = None

    # class-methods w/ class-method "decorators"
    @classmethod
    def getexptypes(cls):
        return cls.EXP_TYPES

    # static-methods do not modify state of class or instance
    # for use when you do not need to access the class
    # putting a global function into the class
    @staticmethod
    def getexplist():
        if Raster.__experimentlist is None:
            Raster.__experimentlist = []
        return Raster.__experimentlist
    # name-spacing and making sure that only one list will ever be generated

    def setdate(self, newdate):
        self.date = newdate

    def __init__(self, date, exptype):
        self.date = date
        if exptype not in Raster.EXP_TYPES:
            raise ValueError(f"{exptype} is not a valid exptype")
        else:
            self.exptype = exptype


R1 = Raster(220802, 'Burrow')
R2 = Raster(220807, 'PPI')
R1.setdate(220805)

print(R1.date)
print('exptype: ' + str(R1.exptype))

print('GetExpTypes: ' + str(Raster.getexptypes()))

theexps = Raster.getexplist()
theexps.append(R1)
theexps.append(R2)
print(theexps)
