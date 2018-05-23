import importlib
import random
import lect10


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



degrees = (2, 4, 8, 16)
random.seed(0)
xVals1, yVals1 = getData('data/myData.txt')
xVals2, yVals2 = getData('data/myData2.txt')
models1 = lect10.genFits(xVals1, yVals1, degrees)
models2 = lect10.genFits(xVals2, yVals2, degrees)
# CROSS VALIDATION, testing model 1, with x and y of model 2 and vice-versa
lect10.testFits(models1, degrees, xVals2, yVals2, 'Dataset 2 / Model 1')
lect10.testFits(models2, degrees, xVals1, yVals1, 'Dataset 1 / Model 2')
