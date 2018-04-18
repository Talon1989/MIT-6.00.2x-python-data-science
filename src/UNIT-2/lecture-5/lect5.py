import random


def rollDie():
    """
    :return: random int between 1 and 6
    """
    return random.choice([1,2,3,4,5,6])


def testRoll(n=10):
    result = ''
    for _ in range(n):
        result += str(rollDie()) + ' '
    return result


def runSimulation(goal='11111', numTrials=1000):
    """
    :param goal: string representing results in dice rolls, es: 11111
    :param numTrials: number of times dice rolls
    :return: void
    """
    total = 0
    for i in range(numTrials):
        result = ''
        for _ in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    # 6 sides / outputs of dice
    print('Actual probability =', round(1 / 6 ** len(goal), 8))
    print('Estimated probability =', round(total / numTrials, 8))


def fracBoxCars(numTests):  # box cars = 2 dadi = 6, 6   probability is 1/36  6**2
    numBoxCars = 0
    for _ in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars / numTests


# print(testRoll())
runSimulation()
print()
print('frequency of double 6 =', fracBoxCars(100000)*100, '%')

random.seed(0)
for _ in range(5):
    print(random.random())