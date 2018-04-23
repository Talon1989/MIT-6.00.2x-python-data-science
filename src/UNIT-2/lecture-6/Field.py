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