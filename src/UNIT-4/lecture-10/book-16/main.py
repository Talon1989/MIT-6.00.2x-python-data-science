import random

import pylab
from enum import Enum


class Impression(Enum):
    flat = 'flat'
    volatile = 'volatile'
    fair = 'fair'


def plotHousing(impression):
    assert isinstance(impression, Impression)
    print(impression.value)
    file = open('midWestHousingPrices.txt', 'r')
    file.readline()
    labels, prices = [], []
    for line in file:
        year, quarter, price = line.split()
        labels.append(year[2:4]+' Q='+quarter[-1:])  # [-1:] = last value
        prices.append(float(price) / 1000)  # in k
    quarters = pylab.arange(len(labels))  #  ==  pylab.array([i for i in range(len(labels))])
    if impression.value == 'flat':
        pylab.semilogy()
    pylab.bar(quarters, prices, width=0.8)
    pylab.title('Housing Prices in U.S. Midwest '+str(impression.value))
    pylab.xlabel('quarter')
    pylab.ylabel('$ in Ks')
    if impression.value == 'flat':
        pylab.ylim(10, 10**3)
    elif impression.value == 'volatile':
        pylab.ylim(180, 220)
    elif impression.value == 'fair':
        pylab.ylim(150, 250)
        pass
    else:
        raise ValueError
    pylab.show()


def juneProbability(tries):
    june48 = 0
    for _ in range(tries):
        june = 0
        for _ in range(446):
            if random.randint(1, 12) == 6:
                june += 1
        if june >= 48:
            june48 += 1
    print('mean probability of 48 june births out of 446:'
          , june48 / tries * 100, '%')


# plotHousing(Impression.fair)
# plotHousing(Impression.volatile)
# plotHousing(Impression.flat)

random.seed(0)
juneProbability(1000)