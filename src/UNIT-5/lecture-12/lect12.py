import matlab
import pylab


class Animal:

    def __init__(self, name, features):
        """
        :param name: str
        :param features: array of [egg-laying, scales, poisonous, cold-blood, legs, reptile]
        """
        self.name = name
        self.features = pylab.array(features)

    def minkowskiDist(self, otherAnimal, degree):
        """
        :param otherAnimal: animal.cls
        :param degree: int, degree of search
        :return: minkowski distance
        """
        v1 = self.getFeatures()
        v2 = otherAnimal.getFeatures()
        dist = 0.0
        for i in range(len(v1)):
            dist += abs(v1[i] - v2[i]) ** degree
        return dist ** (1/degree)

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def __str__(self):
        return self.name


cobra = Animal('cobra', [1,1,1,1,0])
rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa\nconstrictor', [0,1,0,1,0])
chicken = Animal('chicken', [1,1,0,1,2])
alligator = Animal('alligator', [1,1,0,1,4])
dartFrog = Animal('dart frog', [1,0,1,0,4])
zebra = Animal('zebra', [0,0,0,0,4])
python = Animal('python', [1,1,0,1,0])
guppy = Animal('guppy', [0,1,0,0,0])
animals = [cobra, rattlesnake, boa, chicken, guppy,
           dartFrog, zebra, python, alligator]



# a1, a2 = cobra, boa
# print('quadratic minkowski distance between',a1,'and',a2,'='
#       , Animal.minkowskiDist(a1, a2, 2))


# SUPERVISED ALGORITHMS

def zScaleFeatures(vals):
    """
    :param vals: sequence of floats
    :return: zScale
    """
    result = pylab.array(vals)
    mean = sum(result) / len(result)
    return (result - mean) / pylab.std(result)

def isScaleFeatures(vals):
    """
    :param vals: sequence of floats
    :return: scale features
    """
    minVal, maxVal = min(vals), max(vals)
    fit = pylab.polyfit([minVal, maxVal], [0, 1], 1)
    return pylab.polyfit(fit, vals)


