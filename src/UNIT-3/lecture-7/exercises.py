def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) is 0:
        return float('NaN')
    avgLength = sum([len(a) for a in L]) / len(L)
    tot = 0
    for s in L:
        tot += ( len(s) - avgLength ) ** 2
    return ( tot / len(L) ) ** 0.5


def coefficientOfVariation(listOfNumbers):
    """
    :param listOfNumbers: list of numbers
    :return: coefficient of variation
    """
    mean = sum(listOfNumbers) / len(listOfNumbers)
    tot = 0.0
    for n in listOfNumbers:
        tot += (n-mean) ** 2
    sigma = ( tot / len(listOfNumbers) ) ** 0.5
    return sigma / mean


print(coefficientOfVariation([10, 4, 12, 15, 20, 5]))
