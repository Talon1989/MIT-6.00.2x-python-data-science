import pylab



def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline()  # discard header
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return masses, distances


def avgMeanSquareError(data, predicted):
    error = 0.0
    for i in range(len(data)):
        error += (data[i] - predicted[i]) ** 2
    return error / len(data)


def coefficientOfDetermination(data, predicted):
    mean = sum(data) / len(data)
    nominator = 0.0
    denominator = 0.0
    for i in range(len(data)):
        nominator += (data[i] - predicted[i]) ** 2
        denominator += (data[i] - mean) ** 2
    return 1 - nominator / denominator


# polyFit

def fitData(fileName):

    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals) * 9.81  # get F * gravity, x is the mass of the spring
    yVals = pylab.array(yVals)
    pylab.plot(xVals, yVals, 'bo', label='Measured points')

    pylab.title('MIT Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

    a, b = pylab.polyfit(xVals, yVals, 1)  # 1 since it's linear, return coefficients of polynomials
    estYVals = a*xVals + b
    print('a =', a, '; b =', b)
    # k == spring constant
    pylab.plot(xVals, estYVals, 'r', label='Linear fit, k = '+str(round(1/a, 5)))
    pylab.legend(loc='best')
    pylab.show()


def fitData1(fileName, p=1):

    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals) * 9.81  # get F * gravity, x is the mass of the spring
    yVals = pylab.array(yVals)
    pylab.plot(xVals, yVals, 'bo', label='Measured points')
    pylab.title('MIT Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

    model = pylab.polyfit(xVals, yVals, p)
    print('model =', model)
    estYVals = pylab.polyval(model, xVals)
    pylab.plot(xVals, estYVals, 'r',
               label='Fit, k = '+str(round(1/model[0], 5)))
    pylab.legend(loc='best')
    pylab.show()

    print('avg mean square error for this model = '
          , avgMeanSquareError(yVals, estYVals))


def genFits(xVals, yVals, degrees):
    models = []
    for d in degrees:
        models.append(pylab.polyfit(xVals, yVals, d))
    return models


def testFits(models, degrees, xVals, yVals, title='No Title'):
    pylab.plot(xVals, yVals, 'o', label='Data')
    for i in range(len(models)):
        estYVals = pylab.polyval(models[i], xVals)
        error = coefficientOfDetermination(yVals, estYVals)
        pylab.plot(xVals, estYVals,
            label='Fit of degree '+str(degrees[i])+' R2 = '+str(round(error,5)))
    pylab.legend()
    pylab.title(title)
    pylab.show()


# fitData1('mysteryData.txt', 2)

# xs, ys = getData('mysteryData.txt')
# degreess = 1, 2, 3
# modelss = genFits(xs, ys, degreess)
# testFits(modelss, degreess, xs, ys, 'Mystery Data')