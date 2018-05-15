import random


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    sameColor = 0
    for _ in range(numTrials):
        bucket = ['r','r','r','g','g','g']
        balls = []
        for _ in range(3):
            unit = random.choice(bucket)
            balls.append(unit)
            bucket.remove(unit)
        if balls == ['r','r','r'] or balls == ['g','g','g']:
            sameColor += 1
    return sameColor / numTrials


# done
print(noReplacementSimulation(100))
