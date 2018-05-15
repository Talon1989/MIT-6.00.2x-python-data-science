import random

import pylab
import scipy.integrate

from RouletteCls import FairRoulette, AmRoulette, EuRoulette


def playRoulette(game, numSpins, toPrint=True):
    """
    :param game: roulette
    :param numSpins: number of plays / spins
    :param toPrint: boolean toPrint
    :return: a tuple of 3 numbers, returning money from bets
    """
    luckyNumber = '2'
    bet = 1
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0
    for i in range(numSpins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting red ='+str(100*(totRed/numSpins))+'%')
        print('Expected return betting black ='+str(100*(totBlack/numSpins))+'%')
        print('Expected return betting', luckyNumber, '=',
              str(100*(totPocket/numSpins))+'%\n')
    return totRed/numSpins, totBlack/numSpins, totPocket/numSpins


def findPocketReturns(game, numTrials, trialSize, toPrint=False):
    pocketReturns = []
    for t in range(numTrials):
        pocketReturns.append(
            playRoulette(game, trialSize, toPrint) [2]  # [2] is totPocket/numSpins
        )
    return pocketReturns


def getMeanAndStd(X):  #  std = standard deviation, small sigma
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


def testRouletteWEmpiricalRule(numTrials):
    resultDict = {}
    games = (FairRoulette, EuRoulette, AmRoulette)
    for g in games:
        resultDict[g().__str__()] = []
    for spins in (100, 1000, 10000, 100000):
        print('\nSimulate betting a pocket for', numTrials, 'trials of', spins, 'spins each')
        for g in games:
            pocketReturns = findPocketReturns(g(), numTrials, spins, False)
            mean, std = getMeanAndStd(pocketReturns)
            resultDict[g().__str__()].append( (spins, 100*mean, 100*std) )
            print('Exp. return for', g(), '=',
                  str(round(mean*100, 3)) + '% +/- ' + str(round(std*1.96*100,3))
                  + '% with 95% confidence')


# random.seed(0)
# numTrials = 20
# testRouletteWEmpiricalRule(numTrials)

# ------------ CHECKING EMPIRICAL RULE ------------

def gaussian(x, mu, sigma):
    factor1 = ( 1.0 / ( sigma * ( ( 2 * pylab.pi ) ** 0.5 ) ) )
    factor2 = pylab.e ** -( ( ( x - mu ) ** 2 ) / ( 2 * ( sigma ** 2 ) ) )
    return factor1 * factor2


def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu=', mu, 'and sigma =', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(
                gaussian,  #  function
                mu - (numStd * sigma),  # lower limit, 'a'
                mu + (numStd * sigma),  # upper limit, 'b'
                (mu, sigma)  # other, non 'x' arguments
            )[0]
            print( ' Fraction within', numStd, 'std =', round(area, 4) )


# checkEmpirical(3)

