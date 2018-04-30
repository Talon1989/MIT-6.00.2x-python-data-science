import pylab
import random

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L
    """
    bests = []
    for n1 in range(0, len(L)):
        iterationNumbers = []
        current = 0
        for n2 in range(n1, len(L)):
            current += L[n2]
            iterationNumbers.append(current)
        bests.append(max(iterationNumbers))
    return max(bests)


# nums =  [3, 4, -8, 15, -1, 2]
# print(max_contig_sum(nums))


def graphs(nodes):
    xVals = []
    yVals = []
    for i in range(len(nodes)):
        x = nodes[i]
        y = nodes[i]
        print(x)
        xVals.append(x)
        yVals.append(y)
    pylab.scatter(xVals, yVals)
    pylab.show()


# graphs([5,7,6,15,2,3,10])


def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    for n in range(2000):
        if test(n) is True:
            return n
        elif test(-n) is True:
            return -n
    return None


#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))


#### This test case prints 0 ####
def g(x):
    return x == 0
print(solveit(g))

def e(x):
    return [1, 2, 3][-x] == 1 and x != 0
print(solveit(e))


# print(f(15))


