# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


# def yieldAllCombos(items):
#     """
#       Generates all combinations of N items into two bags, whereby each
#       item is in one or zero bags.
#
#       Yields a tuple, (bag1, bag2), where each bag is represented as
#       a list of which item(s) are in each bag.
#     """
#     N = len(items)
#     for i in range(3**N):



s = [1, 2, 3, 4, 5, 6]
combinations = 0
for p in powerSet(s):
    combinations += 1

print('set length :', len(s))
print('combinations :', combinations)



# for i in range(10**2):
#     for j in range(2):
#         print('{0:b}'.format(i), '>>', '{0:b}'.format(j), '=', '{0:b}'.format(i >> j)
#               , '=', i >> j)


