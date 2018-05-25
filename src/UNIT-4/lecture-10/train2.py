import pylab
import random


def getDiceData(tries):
    oneRoll = []
    tenRolls = []
    for _ in range(tries):
        one = random.randint(0,5)
        ten = 0
        for _ in range(10):
            ten += random.randint(0,5)
        ten /= 10
        oneRoll.append(one)
        tenRolls.append(ten)
    return oneRoll, tenRolls


def plotDices(oneRoll, tenRolls):
    weightOne = pylab.array(len(oneRoll) * [1]) / len(oneRoll)
    weightTen = pylab.array(len(tenRolls) * [1]) / len(tenRolls)
    pylab.hist(oneRoll, label='means of one roll', bins=20
               , weights=weightOne)
    pylab.hist(tenRolls, label='means of ten rolls', bins=20
               , weights=weightTen)
    pylab.xlabel('means')
    pylab.ylabel('events')
    pylab.legend()
    pylab.show()


ones, tens = getDiceData(100000)
plotDices(ones, tens)