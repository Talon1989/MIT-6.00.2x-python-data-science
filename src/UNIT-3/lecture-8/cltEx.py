import random

import pylab


def getMeanAndStd(X):
    """
    :param X: list of data, numbers
    :return: tuple of mean and standard deviation
    """
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x-mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


# zeroOneNumbers = []
# for _ in range(100000):  # populate of numbers between 0.3 and 0.7
#     zeroOneNumbers.append(random.uniform(0.3,0.7))
# print(getMeanAndStd(zeroOneNumbers))
# print(getMeanAndStd(zeroOneNumbers[3000:4000]))


zeroOneNumbers = []
zeroOneNumbers2 = []
for _ in range(10000):  # populate of numbers between 0.3 and 0.7
    num = 0.0
    num2 = 0.0
    for _ in range(20):
        num += random.uniform(0.0,1.0)
    zeroOneNumbers2.append(random.uniform(0.0, 1.0))
    # append the mean of 20 rolls
    zeroOneNumbers.append(num / 20)
pylab.hist(zeroOneNumbers,
           weights=pylab.array(len(zeroOneNumbers)*[1]) / len(zeroOneNumbers))
pylab.hist(zeroOneNumbers2,
           weights=pylab.array(len(zeroOneNumbers2)*[1]) / len(zeroOneNumbers2))
pylab.show()
