import pylab


# PYLAB BABY

def plotting():
    mySamples = []
    myLinear = []
    myQuadratic = []
    myCubic = []
    myExponential = []
    for i in range(0, 30):
        mySamples.append(i)
        myLinear.append(i)
        myQuadratic.append(i ** 2)
        myCubic.append(i ** 3)
        myExponential.append(1.5 ** i)

    pylab.figure('lin')
    pylab.title('Linear')
    pylab.xlabel('sample points')
    pylab.ylabel('linear function')
    pylab.plot(mySamples, myLinear)
    pylab.show()  # show the graph, required in pycharm
    pylab.clf()  # clear / ends the frame

    pylab.figure('quad')
    pylab.title('Quadratic')
    pylab.xlabel('sample points')
    pylab.ylabel('quadratic function')
    pylab.plot(mySamples, myQuadratic)
    pylab.show()
    pylab.clf()

    pylab.figure('cube')
    pylab.title('Cubic')
    pylab.xlabel('sample points')
    pylab.ylabel('cubic function')
    pylab.plot(mySamples, myCubic)
    pylab.show()
    pylab.clf()

    pylab.figure('expo')
    pylab.title('Exponential')
    pylab.xlabel('sample points')
    pylab.ylabel('exponential function')
    pylab.plot(mySamples, myExponential)
    pylab.show()
    pylab.clf()


def plottingWithLimits():
    mySamples = []
    myLinear = []
    myQuadratic = []
    myCubic = []
    myExponential = []
    for i in range(0, 30):
        mySamples.append(i)
        myLinear.append(i)
        myQuadratic.append(i ** 2)
        myCubic.append(i ** 3)
        myExponential.append(1.5 ** i)

    pylab.figure('lin')
    pylab.clf()
    pylab.ylim(0, 1000)  # limits the y axis to a range(0, 1000)
    pylab.title('Linear')
    pylab.xlabel('sample points')
    pylab.ylabel('linear function')
    pylab.plot(mySamples, myLinear)
    pylab.show()

    pylab.figure('quad')
    pylab.clf()
    pylab.ylim(0, 1000)
    pylab.title('Quadratic')
    pylab.xlabel('sample points')
    pylab.ylabel('quadratic function')
    pylab.plot(mySamples, myQuadratic)
    pylab.show()

    pylab.figure('cube')
    pylab.clf()
    pylab.ylim(0, 1000)
    pylab.title('Cubic')
    pylab.xlabel('sample points')
    pylab.ylabel('cubic function')
    pylab.plot(mySamples, myCubic)
    pylab.show()

    pylab.figure('expo')
    pylab.clf()
    pylab.ylim(0, 1000)
    pylab.title('Exponential')
    pylab.xlabel('sample points')
    pylab.ylabel('exponential function')
    pylab.plot(mySamples, myExponential)
    pylab.show()


functions = {
    'mySamples' : [],
    'myLinear' : [],
    'myQuadratic': [],
    'myCubic': [],
    'myExponential': []
}
for i in range(0, 30):
    functions['mySamples'].append(i)
    functions['myLinear'].append(i)
    functions['myQuadratic'].append(i ** 2)
    functions['myCubic'].append(i ** 3)
    functions['myExponential'].append(1.5 ** i)


def plottingWithOverlaysLegendAndColors(funcs):
    """
    :param funcs: dictionary of arrays
    :return: void
    """
    assert isinstance(funcs, dict)

    pylab.figure('lin-quad')
    pylab.clf()
    # pylab.ylim(0, 1000)
    pylab.title('Linear vs Quadratic')
    pylab.xlabel('sample')
    pylab.ylabel('function')
    pylab.plot(funcs['mySamples'], funcs['myLinear'],
               '--b', label='linear')
    pylab.plot(funcs['mySamples'], funcs['myQuadratic'],
               'ro', label='quadratic')
    pylab.legend(loc='upper left')
    pylab.show()

    pylab.figure('cube-exp')
    pylab.clf()
    # pylab.ylim(0, 1000)
    pylab.title('Cubic vs Exponential')
    pylab.xlabel('sample')
    pylab.ylabel('function')
    pylab.plot(funcs['mySamples'], funcs['myCubic'],
               linewidth=2.0, label='cubic')
    pylab.plot(funcs['mySamples'], funcs['myExponential'],
               linewidth=5.0, label='exponential')
    pylab.legend(loc='upper left')
    pylab.show()


def plottingWithOverlaysLegendAndColorsAndSubplots(funcs):
    """
    :param funcs: dictionary of arrays
    :return: void
    """
    assert isinstance(funcs, dict)

    pylab.figure('lin-quad')
    pylab.clf()
    pylab.subplot(211)  # a,b,c  =  n-rows,n-columns,location to use
    pylab.ylim(0, 900)
    pylab.plot(funcs['mySamples'], funcs['myLinear'],
               'b-', label='linear')
    pylab.legend(loc='upper left')
    pylab.show()
    pylab.subplot(212)
    pylab.ylim(0, 900)
    pylab.plot(funcs['mySamples'], funcs['myQuadratic'],
               'r', label='quadratic')
    pylab.legend(loc='upper left')
    pylab.title('Linear vs Quadratic')
    pylab.show()


def plottingInLogScale(funcs):
    pylab.figure('cube exp')
    pylab.clf()
    pylab.plot(funcs['mySamples'], funcs['myCubic'],
               'r', label='cubic')
    pylab.plot(funcs['mySamples'], funcs['myExponential'],
               'r', label='expo')
    pylab.yscale('log')  # setting the y axis log scale, mimics the expo function
    pylab.show()


plottingInLogScale(functions)