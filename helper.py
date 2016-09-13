import random


class Dice(object):
    def __init__(self, sides=6, start=1):
        super().__init__()
        self._sides = sides
        self._start = start

    def roll(self):
        return random.randint(self._start, self._sides + self._sides - 1)



