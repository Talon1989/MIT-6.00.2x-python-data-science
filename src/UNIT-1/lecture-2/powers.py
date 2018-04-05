

def iterativePowerSet(xs):
    result = [[]]
    for x in xs:
        newSubset = [subset + [x] for subset in result]
        result.extend(newSubset)
        yield result


def originalPowerSet(orig, newSet):
    if orig == []:
        return [newSet]
    else:
        res = []
        for s in originalPowerSet(orig[1:], newSet+[orig[0]]):
            res.append(s)
        for s in originalPowerSet(orig[1:], newSet):
            res.append(s)
        return res


def originalPowerSetYield(orig, newSet):
    if not orig:  # same as origin == []
        yield newSet
    else:
        print('printing', orig)
        for s in originalPowerSetYield(orig[1:], newSet+[orig[0]]):
            yield s
        for s in originalPowerSetYield(orig[1:], newSet):
            yield s


def powerSet4(lst):
    if len(lst) < 2:
        yield lst
        yield []
    else:
        for x in powerSet4(lst[1:]):
            yield [lst[0]] + x
            yield x


def powerSet5(lst):
    if not lst:  # same as lst == []
        yield []
    else:
        for s in powerSet5(lst[1:]):
            yield s + [lst[0]]
            yield s


def powerSet6(lst):
    pairs = [(2**i, x) for i, x in enumerate(lst)]
    for i in range(2**len(pairs)):
        yield [x for (mask, x) in pairs if i & mask]


se = [1, 2, 3, 4]
for p in iterativePowerSet(se):
    print(p)

print('originalPowerSetYield')

for p in originalPowerSetYield(se, []):
    print(p)

print('powerSet4')

for p in powerSet4(se):
    print(p)

print('powerSet5')

for p in powerSet5(se):
    print(p)

print('powerSet6')

for p in powerSet6(se):
    print(p)