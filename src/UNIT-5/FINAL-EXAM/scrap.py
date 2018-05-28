
import random, pylab, numpy as np


def drawing_without_replacement_sim(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    """
    results = []
    for _ in range(numTrials):
        bucket = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
        result = []
        for _ in range(3):
            ball = random.choice(bucket)
            bucket.remove(ball)
            result.append(ball)
        results.append(result)
    counter = 0
    for r in results:
        if r == ['r', 'r', 'r'] or r == ['g', 'g', 'g']:
            counter += 1
    return counter / len(results)


import itertools
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    combinations = np.array(
        list(itertools.product([0,1], repeat=len(choices)))
    )
    bestResult = []
    noExact = []
    closest = 99999999
    smallest = 99999999
    for c in combinations:
        value = sum(c * choices)
        if value == total and sum(c) < smallest:
            bestResult = c
            smallest = sum(c)
        elif 0 < total - value < closest:
            # print('aa')
            # print(c)
            closest = total - value
            noExact = c
    return bestResult if len(bestResult) > 0 else noExact





# print(drawing_without_replacement_sim(1000))
print(find_combination([1, 3, 4, 2, 5], 16))