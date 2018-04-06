import lect1
from Food import Food

# BRUTE-FORCE ALGORITHM


def maxVal(toConsider, available):
    """
    :param toConsider: list of items
    :param available: a weight
    :return: tuple of total value of a solution to 0/1 knapsack and the items
    """
    print('toConsider len:', len(toConsider), ' | available:', available)
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


def testMaxVal(foods, maxUnits, printItems=True):
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
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