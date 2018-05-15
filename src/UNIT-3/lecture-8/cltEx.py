import random


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


zeroOneNumbers = []
for _ in range(100000):  # populate of numbers between 0.3 and 0.7
    zeroOneNumbers.append(random.uniform(0.3,0.7))
print(getMeanAndStd(zeroOneNumbers))
print(getMeanAndStd(zeroOneNumbers[3000:4000]))

