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


print(testRoll())