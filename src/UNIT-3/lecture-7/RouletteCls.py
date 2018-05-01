import random


class FairRoulette:

    def __init__(self):
        self.pockets = [i for i in range(1, 37)]
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len(self.pockets) - 1.0

    def spin(self):
        self.ball = random.choice(self.pockets)

    def isBlack(self):
        if type(self.ball) is not int:
            return False
        if (0 < self.ball <= 10) or (18 < self.ball <= 28):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1

    def isRed(self):
        return type(self.ball) is int and not self.isBlack()

    def betBlack(self, amt):
        if self.isBlack():
            return amt * self.blackOdds
        else:
            return -amt

    def betRed(self, amt):
        if self.isRed():
            return amt * self.redOdds
        else:
            return -amt

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return 'Fair Roulette'


class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'


class AmRoulette(EuRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return 'American Roulette'


