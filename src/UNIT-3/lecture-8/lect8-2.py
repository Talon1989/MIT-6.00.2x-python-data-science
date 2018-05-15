import random

def stdDev(X):
    tot = 0.0
    mean = sum(X) / len(X)
    for x in X:
        tot += (x-mean) ** 2
    return (tot / len(X)) ** 0.5


def throwNeedles(numNeedles):
    inCircle = 0
    for _ in range(1, numNeedles+1, 1):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) ** 0.5 <= 1:  # x**2 + y**2 = hypotenuse**2, since radius is one, if it's more than 1 is outside of the circle
            inCircle += 1
    return (4 * inCircle) / numNeedles


def getEstimate(numNeedles, numTrials):
    estimates = []
    for _ in range(numTrials):
        estimates.append(throwNeedles(numNeedles))
    sDev = stdDev(estimates)
    curEst = sum(estimates) / len(estimates)
    print('Est. =', curEst, ' , Std. dev. =', sDev, ' , Needles =', numNeedles)
    return curEst, sDev


def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision / 2:
        curEst, sDev = getEstimate(numNeedles, numTrials)
        numNeedles *= 2
    return curEst


estPi(0.0005, 100)