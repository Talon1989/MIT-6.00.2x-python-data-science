import pylab
import random


def makeGraph(xVals, yVals, title=''):
    pylab.plot(xVals, yVals)
    pylab.title(title)
    pylab.legend()
    pylab.show()


def populateData(fName):
    xVals = range(-15, 26, 1)
    a, b, c = 3, 0, 0
    yVals = []
    for x in xVals:
        value = a*x**2 + b*x**1 + c
        yVals.append(value + random.gauss(0, 10))
    file = open(fName, 'w')
    file.write('x      y\n')
    for n in range(len(xVals)):
        file.write(str(xVals[n]) + ' ' + str(yVals[n]) + '\n')
    file.close()


def getData(fName):
    file = open(fName, 'r')
    file.readline()
    xVals, yVals = [], []
    for line in file:
        x, y = line.split(' ')
        xVals.append(float(x))
        yVals.append(float(y))
    file.close()
    return pylab.array(xVals), pylab.array(yVals)


# populateData('data2.txt')


# -----------------------------------------------------------


def r2(givenYs, predictedYs):
    """
    :param givenYs: pylab.array()
    :param predictedYs: pylab.array()
    :return: coefficient of determination
    """
    mean = sum(givenYs) / len(givenYs)
    estimatedError = ((givenYs - predictedYs) ** 2).sum()
    estimatedVariability = ((givenYs - mean) ** 2).sum()
    return 1 - estimatedError / estimatedVariability


def splitSamples(xVals, yVals):
    toTrain = random.sample( range(len(xVals)), len(xVals)//2 )
    trainX, trainY, testX, testY = [], [], [], []
    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])
    return trainX, trainY, testX, testY


def test():
    # xVals, yVals = getData('data2.txt')
    # trainX, trainY, testX, testY = splitSamples(xVals, yVals)
    # makeGraph(trainX, trainY)
    # makeGraph(testX, testY)
    rSquares = {}
    dimensions = 1, 2, 3
    for n in dimensions:
        rSquares[n] = []
    tries = 10
    xVals, yVals = getData('data2.txt')
    for t in range(tries):
        trainX, trainY, testX, testY = splitSamples(xVals, yVals)
        for d in dimensions:
            model = pylab.polyfit(trainX, trainY, d)
            predictedYs = pylab.polyval(model, testX)
            rSquares[d].append(r2(testY, predictedYs))
    for d in dimensions:
        print('mean r2 for', d, 'dimensions =', sum(rSquares[d]) / len(rSquares[d]))
        print('std for', d, 'dimensions =', pylab.std(rSquares[d]))
        print()





# xs, ys = getData('data1.txt')
# model = pylab.polyfit(xs, ys, 2)
# predictedY = pylab.polyval(model, xs)
# pylab.plot(xs, ys, label='Data')
# pylab.plot(xs, predictedY, label='Predicted Data')
# pylab.legend()
# pylab.show()
# print(r2(ys, predictedY))

test()
