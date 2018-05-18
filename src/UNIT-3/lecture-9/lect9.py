import numpy
import pylab
import random


def makeHistogram(data, title, xlabel, ylabel, bins=20):
    pylab.hist(data, bins=bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)


def getHighs(file):
    inFile = open(str(file))
    population = []
    for l in inFile:
        try:
            tempC = float(l.split(',')[1])
            population.append(tempC)
        except ValueError:
            continue
    return population


def getMeansAndSds(population, sample, verbose=False):
    popMean = sum(population) / len(population)
    sampleMean = sum(sample) / len(sample)
    if verbose:
        makeHistogram(population, 'Daily High 1961-2015 Population mean = '+
                      str(round(popMean, 2)), 'Degrees C', 'Number Days')
        pylab.axvline(x=popMean, color='r')
        pylab.show()
        pylab.figure()
        makeHistogram(sample, 'Daily High 1961-2015 Sample mean = '+
                      str(round(sampleMean, 2)), 'Degrees C', 'Number Days')
        pylab.axvline(x=popMean, color='r')
        pylab.show()
    return popMean, sampleMean, numpy.std(population), numpy.std(sample)


def sample1000(population, sampleSize):
    sampleMeans = []; maxMeanDiff = 0; maxSDDiff = 0
    for _ in range(1000):
        sample = random.sample(population, sampleSize)
        popMean, sampleMean, popSD, sampleSD = getMeansAndSds(population, sample, False)
        sampleMeans.append(sampleMean)
        if abs(popMean-sampleMean) > maxMeanDiff:
            maxMeanDiff = abs(popMean-sampleMean)
        if abs(popSD-sampleSD) > maxSDDiff:
            maxSDDiff= abs(popSD-sampleSD)
    makeHistogram(sampleMeans, 'Mean of Samples', 'Mean', 'Frequency')
    pylab.axvline(x=popMean, color='r')
    pylab.show()
    print('Mean of sample of Means ='
          ,round(sum(sampleMeans)/len(sampleMeans),3))
    print('STD of sample of Means ='
          ,round(numpy.std(sampleMeans),3))
    print('Maximum difference in mean =', round(maxMeanDiff, 3))
    print('Maximum difference in std =',round(maxSDDiff, 3))


def testStandardErrorOfMean():
    # sem = σ(sample) / len(sample) ** 0.5
    def sem(s, size):
        return s / size ** 0.5
    sampleSizes = (25, 50, 100, 200, 300, 400, 500, 600)
    numTrials = 50
    population = getHighs('temperatures.csv')
    popSD = numpy.std(population)
    sems = []
    sampleSDS = []
    for siz in sampleSizes:
        sems.append(sem(popSD, siz))
        means = []
        for _ in range(numTrials):
            sample = random.sample(population, siz)
            means.append(sum(sample) / siz)  # siz == len(sample)
        sampleSDS.append(numpy.std(means))
    pylab.plot(sampleSizes, sampleSDS, label='Std of 50 means')
    pylab.plot(sampleSizes, sems, 'r--', label='SEM')
    pylab.title('SEM vs. SD for 50 Means')
    pylab.legend()
    pylab.show()


def plotDistributions():
    uniform, normal, exp = [], [], []
    for _ in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0,1))
        exp.append(random.expovariate(0.5))
    makeHistogram(uniform, 'Uniform', 'Value', 'Frequency')
    pylab.show()
    pylab.figure()
    makeHistogram(normal, 'Normal', 'Value', 'Frequency')
    pylab.show()
    pylab.figure()
    makeHistogram(exp, 'Exponential', 'Value', 'Frequency')
    pylab.show()
    pylab.figure()


# ---------------------------------------------------------


def tempsWithSamples(sampleSize):
    temps = getHighs('temperatures.csv')
    popMean = sum(temps) / len(temps)
    numTrials = 10000
    numBad = 0
    for _ in range(numTrials):
        sample = random.sample(temps, sampleSize)
        sampleMean = sum(sample) / len(sample)
        # mean of the single sample, not the sample of mean samples
        se = numpy.std(sample) / sampleSize ** 0.5
        if abs(popMean - sampleMean) > 1.96 * se:
            numBad += 1
    print('Fraction outside 95% confidence interval =', numBad/numTrials)


# pop = getHighs('temperatures.csv')
# samp = random.sample(pop, 100)
# getMeansAndSds(pop, samp, True)

# sample1000(pop, 200)

testStandardErrorOfMean()

# tempsWithSamples(200)