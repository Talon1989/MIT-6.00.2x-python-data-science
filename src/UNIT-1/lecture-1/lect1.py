from Food import Food

print()


def buildMenu(names, values, calories):
    '''
    :param names: list of str of length x
    :param values: list of int of length x
    :param calories: list of int of length x
    :return: list of appended names, values and calories
    '''
    assert len(names) == len(values) == len(calories)
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def flexibleGreedy(items, maxCost, keyFunction):
    '''
    :param items: list of Food
    :param maxCost: >= 0
    :param keyFunction: maps elements of items to numbers
    :return: tuple of the 'keyFunction' based combination of food and their total value
    '''
    assert isinstance(items, list); assert maxCost >= 0
    itemsCopy = sorted(items, key=keyFunction, reverse=True)  # sorted so it does return a copy of the original
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
        else:
            break
    return result, totalValue


def testGreedy(items, constraint, keyFunction):
    '''
    :param items: list of Food
    :param constraint: >= 0
    :param keyFunction: maps elements of items to numbers
    :return: void
    '''
    taken, val = flexibleGreedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)
    print()


def testGreedys(items, maxUnits):
    '''
    :param items: list of Food
    :param maxUnits: >= 0
    :return:
    '''
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(items, maxUnits, Food.getValue)
    print('Use greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(items, maxUnits, lambda x: 1/Food.getCost(x))  # 1/func so it sort by least expensive to most, Food.getCost sorts by most to least
    print('Use greedy by density to allocate', maxUnits, 'calories')
    testGreedy(items, maxUnits, Food.density)


foods = buildMenu(
    ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut'],
    [89, 90, 95, 100, 90, 79, 50, 10],
    [123, 154, 258, 354, 365, 150, 95, 195]
)

testGreedys(foods, 750)








