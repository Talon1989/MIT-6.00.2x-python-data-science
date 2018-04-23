import random

from Drunk import Drunk
from Drunk import UsualDrunk
from Drunk import ColdDrunk
from Field import Field
from Location import Location


def walk(f, d, steps):
    """
    :param f: instance of Field
    :param d: instance of Drunk
    :param steps: int >= 0, times 'd' moves
    :return: distance between starting and final location
    """
    assert isinstance(f, Field); assert isinstance(d, Drunk)
    start = f.getLoc(d)
    for _ in range(steps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numTrials, numSteps, drunkType):
    """
    :param numTrials: int >= 0, times we append a new "times 'd' moves"
    :param numSteps: int >= 0, times 'd' moves
    :param drunkType: subclass of Drunk
    :return: list of final distances for each trial
    """
    homer = drunkType('drunko')
    distances = []
    for _ in range(numTrials):
        f = Field()
        f.addDrunk(homer, Location(0, 0))
        distances.append(
            round(walk(f, homer, numSteps), 2)
        )
    return distances


def drunkTest(walkLengths, numTrials, drunkType):
    """
    :param walkLengths: tuple of different lengths of steps
    :param numTrials: int >= 0, times we run tries
    :param drunkType: subclass of Drunk
    :return: void
    """
    for numSteps in walkLengths:
        distances = simWalks(numTrials, numSteps, drunkType)
        print(drunkType.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(
            sum(distances) / len(distances), 4
        ))
        print(' Max =', max(distances),' Min =', min(distances))


def simAll(walkLengths, numTrials, drunkKinds):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)


# patatino = UsualDrunk('patatino')
# f1 = Field()
# f1.addDrunk(patatino, Location(0,0))
# print(walk(f1, patatino, 15))
# print()


drunkTest( (10, 100, 1000, 10000), 100, UsualDrunk )