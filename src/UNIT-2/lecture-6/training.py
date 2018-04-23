import pylab
import sys


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)


def combinations(n, k):
    """
    :param n: int >= 0
    :param k: int >= 0
    :return: combinations n choose k
    """
    return factorial(n) / (factorial(k) * factorial(n-k))


# plot 20choose1 > 20choose2 > ... 20choose20


def combinationGraph(size=10):
    sampleList = []
    combinationList = []
    for k in range(size):
        sampleList.append(k)
        combinationList.append(combinations(size, k))
    pylab.plot(sampleList, combinationList)
    pylab.title('Combinations over range')
    pylab.xlabel('k')
    pylab.ylabel('kCn')
    pylab.legend(loc='upper left')
    pylab.show()



sys.setrecursionlimit(10001)
combinationGraph(100)