import pylab


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


print(combinations(30, 15))