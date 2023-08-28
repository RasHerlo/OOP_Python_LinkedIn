
# Create basic classes

class Raster:
    def __init__(self, mouse, experiment, expdate, frames):
        self.mouse = mouse
        self.experiment = experiment
        self.expdate = expdate
        self.frames = frames

    def getdate(self):
        if hasattr(self, "_delay"):
            return self.expdate + self._delay
        else:
            return self.expdate

    def setdelay(self, days):
        self._delay = days


R1 = Raster('EM0420', 'Burrow', 220822, 60000)
R2 = Raster('EM0520', 'PPI', 220905, 60000)

print('ExpDate before delay: ' + str(R1.getdate()))
R1.setdelay(5)
print(R1.mouse)
print('ExpDate after delay: ' + str(R1.getdate()))


