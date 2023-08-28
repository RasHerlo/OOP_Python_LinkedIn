
import numpy as np
import matplotlib.pyplot as plt
import random

# Since all experimental subclasses contain a raster and a locomotion read-out
# We could improve the writing by defining a "Base-Class", and
# inherited the common attributes
class Experiment:
    def __init__(self, raster, locomotion):
        self.raster = raster
        self.locomotion = locomotion


# Making a secondary base-class, since two of the exp-classes share
# three rather than two attributes
class BurrowBased(Experiment):
    def __init__(self, raster, locomotion, position):
        super().__init__(raster, locomotion)
        self.position = position


class BurrowExp(BurrowBased):
    def __init__(self, raster, locomotion, position, pupildil):
        super().__init__(raster, locomotion, position)
        # self.raster = raster
        # self.locomotion = locomotion
        # self.position = position
        self.pupildil = pupildil


class PPIExp(Experiment):
    def __init__(self, raster, locomotion, tone):
        super().__init__(raster, locomotion)
        # self.raster = raster
        # self.locomotion = locomotion
        self.tone = tone


class LickExp(BurrowBased):
    def __init__(self, raster, locomotion, position, reward):
        super().__init__(raster, locomotion, position)
        # self.raster = raster
        # self.locomotion = locomotion
        # self.position = position
        self.reward = reward


r1 = np.random.rand(100, 1000)

plt.imshow(raster)
plt.show()

l1 = np.random.rand(1000)

plt.plot(locomotion)
plt.show()

p1 = np.random.rand(1000)

rew1 = [0]*1000
for i in range(500):
    rew1[i] = 1

rew1 = random.shuffle(rew1)

LE = LickExp(r1, l1, p1, reward)