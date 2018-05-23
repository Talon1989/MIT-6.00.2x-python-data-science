import pylab


def springData():
    dataFile = open('../springData.txt', 'r')
    distances = []
    masses = []
    dataFile.readline()  # discard header
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return masses, distances


def coeffOfDetermination(actualYVals, predictedYVals):
    """
    :param actualYVals: pylab.array()
    :param predictedYVals: pylab.array()
    :return: R^2
    """
    mean = sum(actualYVals) / len(actualYVals)
    estimateError = ((actualYVals - predictedYVals) ** 2).sum()
    estimateVariability = ((actualYVals - mean) ** 2).sum()
    return 1 - estimateError / estimateVariability


x, y = springData()
x = x[:-7]
y = y[:-7]
x = pylab.array(x) * 9.81
y = pylab.array(y)
predictedY = pylab.polyval(pylab.polyfit(x, y, 1), x)
r2 = coeffOfDetermination(y, predictedY)
print('r2 = ',r2)