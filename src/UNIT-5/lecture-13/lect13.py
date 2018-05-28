import random
import matlab

def fallacy():
    numTrials = 100
    numGreater = 0
    numCasesPerYear = 36000
    years = 3
    stateSize = 10000
    communitySize = 10

    communities = stateSize // communitySize
    for _ in range(numTrials):
        locs = matlab.array([0] * communities)
        for _ in range(years * numCasesPerYear):
            locs[random.choice(range(communities))] += 1
        if max(locs) >= 143:
            numGreater += 1
        print(max(locs))
    probability = round(numGreater / numTrials, 4)
    print('Est probability of at least one district having at least 143',
          'cases =', probability)


fallacy()
