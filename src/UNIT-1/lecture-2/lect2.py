import lect1
from Food import Food
import random
import sys

# BRUTE-FORCE ALGORITHM


def maxVal(toConsider, available):
    """
    :param toConsider: list of items
    :param available: a weight
    :return: tuple of total value of a solution to 0/1 knapsack and the items
    """
    # print('toConsider len:', len(toConsider), ' | available:', available)
    if toConsider == [] or available == 0:
        return 0, ()
    nextItem = toConsider[0]
    # If the first object weights more than the current available, do without it
    if nextItem.getCost() > available:
        # Explore right branch only
        result = maxVal(toConsider[1:], available)
    # If the first object is ok, take two branches, one with it and one without it
    else:
        #  Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], available-nextItem.getCost())
        withVal += nextItem.getValue()
        #  Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], available)
        #  Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = withoutVal, withoutToTake
    return result


def testMaxVal(foods, maxUnits, algorithm=maxVal, printItems=True):
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = algorithm(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)


print('\nLECTURE 2\n')


cibo = lect1.buildMenu(
    ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut'],
    [89, 90, 95, 100, 90, 79, 50, 10],
    [123, 154, 258, 354, 365, 150, 95, 195]
)
testMaxVal(cibo, 750)


# ---------------------------------


def buildLargeMenu(numItems, maxValue, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(
            'num-'+str(i),
            random.randint(1, maxValue),
            random.randint(1, maxCost)))
    return items


# for num in (5, 15, 25, 35, 45):
#     print('Try a menu with', num, 'items')
#     menu = buildLargeMenu(num, 90, 250)
#     testMaxVal(menu, 750, printItems=False)


# MAXVAL WITH MEMOIZATION
# need only to check items left to be considered and available weight
# for overlapping subproblems to be true


def fastMaxVal(toConsider, available, memo={}):
    """
    :param memo: dictionary used by recursive calls using tuple
    :param toConsider: list of items
    :param available: a weight
    :return: tuple of total value of a solution to 0/1 knapsack and the items
    """
    if (len(toConsider), available) in memo:  # memo[len, avail]  exists
        result = memo[len(toConsider), available]
    elif toConsider == [] or available == 0:
        return 0, ()
    elif toConsider[0].getCost() > available:
        result = fastMaxVal(toConsider[1:], available, memo)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = fastMaxVal(toConsider[1:], available-nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], available, memo)
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = withoutVal, withoutToTake
    memo[len(toConsider), available] = result
    return result


# raise maximum recursion depth
sys.setrecursionlimit(2000)


for num in (5, 15, 25, 35, 45, 1024):
    print('Try a menu with', num, 'items')
    menu = buildLargeMenu(num, 90, 250)
    testMaxVal(menu, 750, algorithm=fastMaxVal, printItems=False)

