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
        # todo
        print()
    return popMean, sampleMean, numpy.std(population), numpy.std(sample)



population = getHighs('temps.txt')
sample = random.sample(population, 20)
