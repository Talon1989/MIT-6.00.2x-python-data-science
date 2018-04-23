import random

from Drunk import Drunk
from Drunk import UsualDrunk
from Drunk import ColdDrunk
from Field import Field
from Location import Location
from StyleIterator import StyleIterator
import pylab


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
    return Location.distFrom(start, f.getLoc(d))


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


# patatino = UsualDrunk('patatino')
# f1 = Field()
# f1.addDrunk(patatino, Location(0,0))
# print(walk(f1, patatino, 15))
# print()


# similar to drunkTest function but made to work with plotting using only the mean distance
def simDrunk(numTrials, dClass, walkLengths):
    """
    :param walkLengths: tuple of different lengths of steps
    :param numTrials: int >= 0, times we run tries
    :param dClass: subclass of Drunk
    :return: void
    """
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps (', numTrials,'samples )')
        distances = simWalks(numTrials, numSteps, dClass)
        meanDistances.append(sum(distances) / len(distances))
    return meanDistances


def simAll(walkLengths, numTrials, drunkKinds):
    """
    :param walkLengths: tuple of different amount of steps
    :param numTrials: int >= 0, number of tests
    :param drunkKinds: tuple of subclasses of Drunk class
    :return: void
    """
    styleChoice = StyleIterator( ('m-', 'b--', 'g-.') )
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label=dClass.__name__)
    pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
    pylab.xlabel('Random steps')
    pylab.ylabel('Distance from origins')
    pylab.legend(loc='best')
    pylab.show()


def getFinalLocations(numSteps, numTrials, dClass):
    locations = []
    d = dClass('asd')
    for _ in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        for _ in range(numSteps):
            f.moveDrunk(d)
        locations.append(f.getLoc(d))
    return locations


def plotLocations(drunkKinds, numSteps, numTrials):
    styleChoice = StyleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        print('Plotting', dClass.__name__)
        locations = getFinalLocations(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locations:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        # pylab.array() transforms normal arrays/list in pylab array objects
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        meanX = sum(abs(xVals)) / len(xVals)
        meanY = sum(abs(yVals)) / len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                   label=dClass.__name__+' mean abs dist = <'+str(meanX)+', '+str(meanY)+'>')
    pylab.title('Location at End of Walks ('+str(numSteps)+' steps)')
    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc='upper left')
    pylab.show()


# drunkTest( (10, 100, 1000, 10000), 100, ColdDrunk )

# walks = (10, 100, 1000, 10000)
# simAll(walks, 100, (UsualDrunk, ColdDrunk))

random.seed(0)
plotLocations((UsualDrunk, ColdDrunk), 10000, 1000)