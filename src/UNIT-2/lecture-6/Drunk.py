import random


# intended to be inherited
class Drunk:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Drunk named ' + self.name


class UsualDrunk(Drunk):
    def takeStep(self):
        return random.choice(
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0,0.0)]
        )


class ColdDrunk(Drunk):
    def takeStep(self):
        return random.choice(
            [(0.0,0.9), (0.0,-1.1), (1.0, 0.0), (-1.0,0.0)]
        )