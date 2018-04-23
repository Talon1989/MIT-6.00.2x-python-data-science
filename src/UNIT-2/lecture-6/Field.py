import random

from Location import Location


class Field:

    def __init__(self):
        # key = drunk, value = current location
        self.drunks = {}

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        # drunks[drunk] is a Location
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

    def addDrunk(self, drunk, loc):
        """
        :param drunk: drunk to add to dict drunks
        :param loc: current location of drunk
        :return: void
        """
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk.')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        """
        :param drunk:
        :return: Location of drunk
        """
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        else:
            return self.drunks[drunk]


class OddField(Field):

    def __init__(self, numHoles=1000, xRange=100, yRange=100):
        Field.__init__(self)
        # dict: key = tuple x,y ; value = Location()
        self.wormholes = {}
        for _ in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            self.wormholes[(x, y)] = Location(newX, newY)

    # overriding, when drunk falls into a x,y of wormholes dict, teleport it to its value
    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = Location(self.wormholes[x, y])
