import random

import pylab


def fiftyFifty():
    testSample = 1000
    tries = 10
    zeros, ones = 0, 0
    cumulativeArray = []
    for _ in range(tries):
        zeroOnes = pylab.array([-1] * testSample)
        for i in range(testSample):
            if random.random() <= 0.5:
                zeroOnes[i] = 0
            else:
                zeroOnes[i] = 1
        cumulativeArray.extend(zeroOnes)
        zeros += zeroOnes.sum(0)
        ones += len(zeroOnes) - zeroOnes.sum(0)
    print(zeros)
    print(ones)
    pylab.hist(cumulativeArray, weights=pylab.array([1] * len(cumulativeArray)) / len(cumulativeArray))
    pylab.show()


fiftyFifty()