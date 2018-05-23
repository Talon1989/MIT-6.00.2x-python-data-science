import dis

import pylab

# def getData(file):
#     dataFile = open(file, 'r')
#     xVals = []
#     yVals = []
#     dataFile.readline()
#     for line in dataFile:
#         x, y = line.split()
#         xVals.append(float(x))
#         yVals.append(float(y))
#     dataFile.close()
#     return xVals, yVals
#
#
# distance, mass = getData('../springData.txt')
# forces = pylab.array(mass) * 8.91
# forces = forces[:-6]; distance = distance[:-6]
# a, b = pylab.polyfit(forces, distance, 1)
# predictions = a * forces + b
# # predictions = pylab.polyval(pylab.polyfit(forces, distance, 2), forces)
#
#
# pylab.plot(forces, distance, 'o', label='spring data')
# pylab.plot(forces, predictions, 'r', label='spring prediction')
# pylab.xlabel('F')
# pylab.ylabel('distance')
# pylab.legend()
# pylab.show()

def getTrajectoryData(file):
    dataFile = open(file, 'r')
    distances = []
    heights1, heights2, heights3, heights4 = [], [], [], []
    dataFile.readline()
    for line in dataFile:
        d, h1, h2, h3, h4 = line.split()
        distances.append(float(d))
        heights1.append(float(h1))
        heights2.append(float(h2))
        heights3.append(float(h3))
        heights4.append(float(h4))
    dataFile.close()
    return distances, [heights1, heights2, heights3, heights4]


def processTrajectories(file):
    distances, heights = getTrajectoryData(file)
    numTrials = len(heights)
    distances = pylab.array(distances)
    totHeights = pylab.array([0] * len(distances))  # [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    print( totHeights)
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    meanHeights = totHeights / numTrials
    # print(meanHeights)
    pylab.title('Trajectory of Projectile: mean of '+str(numTrials)+' Trials')
    pylab.xlabel('Inches from launch point')
    pylab.ylabel('Inches above launch point')
    pylab.plot(distances, meanHeights, 'ko')
    a,b = pylab.polyfit(distances, meanHeights, 1)
    altitudes = a*distances + b
    pylab.plot(distances, altitudes, 'b',
               label='Linear fit, RSquare='+str(rSquared(meanHeights, altitudes)))
    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*distances**2 + b*distances**1 + c
    pylab.plot(distances, altitudes, 'r',
               label='Quadratic fit, RSquare='+str(rSquared(meanHeights, altitudes)))
    pylab.legend()
    pylab.show()

    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    getHorizontalSpeed(a, b, c, distances[-1], distances[0])


def rSquared(measured, predicted):
    """
    :param measured: one dimensional pylab.array
    :param predicted: one dimensional pylab.array
    :return: coefficient of determination
    """
    estimateError = ((measured - predicted) ** 2).sum()
    meanOfMeasured = measured.sum() / float(len(measured))
    variability = ((measured - meanOfMeasured) ** 2).sum()
    return 1 - estimateError / variability


def getHorizontalSpeed(a, b, c, minX, maxX):
    """
    :param minX: distance in inches
    :param maxX: distance in inches
    :return: horizontal speed in feet/seconds
    """
    inchesPerFoot = 12.0
    xMid = (maxX - minX)/2.0
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*inchesPerFoot  # acceleration of gravity in inches/sec/sec
    t = (2*yPeak/g)**0.5
    print ('Horizontal speed =', int(xMid/(t*inchesPerFoot)), 'feet/sec')



processTrajectories('projectiles.txt')