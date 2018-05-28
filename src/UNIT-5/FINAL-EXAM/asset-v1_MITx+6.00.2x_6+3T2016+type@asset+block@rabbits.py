import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for _ in range(CURRENTRABBITPOP):
        if random.random() <= 1 - (CURRENTRABBITPOP / MAXRABBITPOP):
            CURRENTRABBITPOP += 1

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for _ in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= (CURRENTRABBITPOP / MAXRABBITPOP):
                CURRENTRABBITPOP -= 1
                if random.random() < 1/3:
                    CURRENTFOXPOP += 1
            else:
                if random.random() <= 1/10 and CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1
        else:
            break
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbits = []
    foxes = []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth2()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes


def foxGrowth2():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for _ in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= (CURRENTRABBITPOP / MAXRABBITPOP):
                CURRENTRABBITPOP -= 1
                if random.random() < 1/3:
                    CURRENTFOXPOP += 1
            else:
                if random.random() <= 9/10 and CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1
        else:
            break


MAXRABBITPOP, CURRENTRABBITPOP,CURRENTFOXPOP,numSteps = 1000, 500, 30, 200
rabs, foxs = runSimulation(numSteps)
squareCoeff = pylab.polyfit(range(len(rabs)), rabs, 2)
rabPrediction = pylab.polyval(squareCoeff, range(len(rabs)))
squareCoeff = pylab.polyfit(range(len(foxs)), foxs, 2)
foxPrediction = pylab.polyval(squareCoeff, range(len(foxs)))
pylab.plot(rabs, label='rabbits')
pylab.plot(rabPrediction, label='rabbits polyfit')
pylab.plot(foxs, label='foxes')
pylab.plot(foxPrediction, label='foxes polyfit')
pylab.legend()
pylab.show()