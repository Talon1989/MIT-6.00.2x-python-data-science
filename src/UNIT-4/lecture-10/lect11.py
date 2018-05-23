import pylab
import random
import lect10


def rSquared(yVals, yValsPredicted):
    mean = sum(yVals) / len(yVals)
    estimateError, estimateVariability = 0, 0
    for n in range(len(yVals)):
        estimateError += (yVals[n] - yValsPredicted[n]) ** 2
        estimateVariability += (yVals[n] - mean) ** 2
    estimateError /= len(yVals)
    estimateVariability /= len(yVals)
    return 1 - estimateError / estimateVariability


def getNoisyParabolicData(a, b, c, xVals, fName):
    yVals = []
    for x in xVals:
        theoreticalVal = a*x**2 + b*x**1 + c
        yVals.append(theoreticalVal + random.gauss(0, 35))
    f = open(fName, 'w')
    f.write('x         y\n')
    for i in range(len(yVals)):
        f.write( str(yVals[i]) + ' ' + str(xVals[i]) + '\n')
    f.close()


# parameters for generating data
def generateData(file):
    xVals = range(-10, 11, 1)
    a, b, c = 3, 0, 0
    getNoisyParabolicData(a, b, c, xVals, file)

generateData('data/myData.txt')
generateData('data/myData2.txt')


# get data util
def getData(file):
    xVals = []; yVals = []
    f = open(file, 'r')
    f.readline()
    for line in f:
        print(line)
        y, x = line.split()
        xVals.append(float(x))
        yVals.append(float(y))
    f.close()
    return xVals, yVals


def crossValidation():
    degrees = (2, 4, 8, 16)
    random.seed(0)
    xVals1, yVals1 = getData('data/myData.txt')
    xVals2, yVals2 = getData('data/myData2.txt')
    models1 = lect10.genFits(xVals1, yVals1, degrees)
    models2 = lect10.genFits(xVals2, yVals2, degrees)
    # CROSS VALIDATION, testing model 1, with x and y of model 2 and vice-versa
    lect10.testFits(models1, degrees, xVals2, yVals2, 'Dataset 2 / Model 1')
    lect10.testFits(models2, degrees, xVals1, yVals1, 'Dataset 1 / Model 2')


def fittingQuadraticToPerfectLine():
    xVals = 0, 1, 2, 3
    yVals = 0, 1, 2, 3.5
    pylab.plot(xVals, yVals, label='Actual Values')
    model = pylab.polyfit(xVals, yVals, 2); print(model)
    estYVals = pylab.polyval(model, xVals)
    pylab.plot(xVals, estYVals, 'r--', label='Predicted Values')
    pylab.legend()
    pylab.show()
    print('R-squared = ', lect10.coefficientOfDetermination(yVals, estYVals))


# fittingQuadraticToPerfectLine()

# --------------------------------------------------------------

class TempDatum:
    def __init__(self, s):
        info = s.split(',')
        self.high = float(info[1])
        self.year = int(info[2][0:4])
    def getHigh(self):
        return self.high
    def getYear(self):
        return self.year


def getTempData():
    inFile = open('temperatures.csv')
    data = []
    inFile.readline()
    for l in inFile:
        data.append(TempDatum(l))
    return data


def getYearlyMeans(data):
    """
    :param data: list of TempDatum objects
    :return: list of dictionaries, with year as key and mean temp as value
    """
    years = {}
    for d in data:
        try:
            years[d.getYear()].append(d.getHigh())
        except KeyError:
            years[d.getYear()] = [d.getHigh()]
    for y in years:
        years[y] = sum(years[y]) / len(years[y])
    return years


def splitData(xVals, yVals):
    toTrain = random.sample(range(len(xVals)), len(xVals) // 2)
    trainX, trainY, testX, testY = [], [], [], []
    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])
    return trainX, trainY, testX, testY


def plotTempData():
    data = getTempData()
    years = getYearlyMeans(data)
    xVals , yVals = [], []
    for y in years:
        xVals.append(y)
        yVals.append(years[y])
    # pylab.plot(xVals, yVals, linewidth=4.0)
    # pylab.xlabel('year')
    # pylab.ylabel('mean daily high temperature')
    # pylab.title('Selected US cities')
    # pylab.show()
    numSubsets = 10
    dimensions = 1, 2, 3
    rSquares = {}
    for d in dimensions:
        rSquares[d] = []
    for f in range(numSubsets):
        trainX, trainY, testX, testY = splitData(xVals, yVals)
        for d in dimensions:
            model = pylab.polyfit(trainX, trainY, d)
            estYVals = pylab.polyval(model, testX)
            rSquares[d].append(rSquared(testY, estYVals))
    print('Mean R-squares for test data')
    for d in dimensions:
        mean = round(sum(rSquares[d]) / len(rSquares[d]) , 4)
        sd = round(pylab.std(rSquares[d]) , 4)
        print('For dimensionality', d, 'mean =', mean, 'std =', sd)


random.seed(0)
plotTempData()


