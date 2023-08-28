
class Raster:
    def __init__(self, mouse, frames):
        self.mouse = mouse
        self.frames = frames


class Experiment:
    def __init__(self, mouse, type):
        self.mouse = mouse
        self.type = type


R1 = Raster('EM0420', 16000)
E1 = Experiment('EM0420', 'Burrow')

print(R1 == E1)
print(type(R1) == type(E1))
print(type(E1))

print('isinstance R1 in Raster: ' + str(isinstance(R1, Raster)))
