import random
import pylab

# import lect7
# from RouletteCls import FairRoulette


def getMeanAndStd(X):  #  std = standard deviation, small sigma
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


# die goes from 0 to 5, not 1 to 6
def plotMeans(numDice, numRolls, numBins, legend, color='b', style='*'):
    means = []
    for _ in range(numRolls // numDice):
        vals = 0
        for _ in range(numDice):
            vals += 5 * random.random()
        means.append(vals / float(numDice))
    pylab.hist(means, numBins, color=color, label=legend
               , weights=pylab.array(len(means)*[1]) / len(means), hatch=style)
    return getMeanAndStd(means)


def testCLT():  # checking Central Limit Theorem  ,
    mean, std = plotMeans(1, 1000000, 30, '1 die')
    print('Mean of rolling 1 die =', str(mean), '  Std =', std)
    mean , std = plotMeans(50, 1000000, 30, '50 dice', 'r', '//')
    print('Mean of rolling 50 dice =', str(mean), '  Std =', std)
    pylab.title('Rolling Continuous Dice')
    pylab.xlabel('Value')
    pylab.ylabel('Probability')
    pylab.legend()
    pylab.show()


def testCLTSimple():
    L = [1, 1, 1, 1, 2]
    pylab.hist(L)
    pylab.show()  # x=1 y=4   ,   x=2 y=1
    # print(pylab.array(len(L)*[1]))  # [1, 1, 1, 1, 1]
    factor = pylab.array(len(L)*[1]) / len(L)  # [0.2, 0.2, 0.2, 0.2, 0.2]
    print(factor)
    pylab.figure()
    pylab.hist(L, weights=factor)
    pylab.show()  # x=1 y=0.8   ,   x=2, y=0.2


# def wRoulette():
#     numTrials = 50000
#     numSpins = 2000
#     game = FairRoulette()
#     means = []
#     for _ in range(numTrials):
#         means.append(lect7.findPocketReturns(game, 1
#             , numSpins)[0] / numSpins)
#     pylab.hist(means, bins=19
#             , weights=pylab.array(len(means)*[1]) / len(means))
#     pylab.xlabel('Mean Return')
#     pylab.ylabel('Probability')
#     pylab.title('Expected Return Betting a Pocket')
#     pylab.show()


testCLT()