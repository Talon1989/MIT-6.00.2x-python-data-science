import pylab as plt


def retire(monthly, rate, terms):
    """
    :param monthly: amount put in each month
    :param rate: annual rate of received interest
    :param terms: number of months
    :return: a tuple of 2 lists, the x base and y savings
    """
    savings = [0]  # list of numbers representing money saved each month / y
    base = [0]  # list of numbers each a linear month [0], [1], [2] ... / x
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1+mRate) + monthly]
    return base, savings


def displayRetireWMonthlies(monthlies, rate, terms):
    """
    :param monthlies: array of different amount of deposited money
    :param rate: rate of profit increase
    :param terms: number of months
    :return: void
    """
    plt.figure('retireMonths')
    plt.clf()
    for m in monthlies:
        x, y = retire(m, rate, terms)
        plt.plot(x, y, label=str(m)+'$ per month')
        plt.legend(loc='upper left')
    plt.show()


def displayRetireWRates(monthly, rates, terms):
    """
    :param monthly: amount of money deposited
    :param rates: array of different rates of profit increase
    :param terms: number of months
    :return: void
    """
    plt.figure('retireRates')
    plt.clf()
    for r in rates:
        x, y = retire(monthly, r, terms)
        plt.plot(x, y, label=str(monthly)+' :'+str(r)+'% rate')
        plt.legend(loc='upper left')
    plt.show()


def displayRetireWMonthsAndRates(monthlies, rates, terms):
    """
    :param monthlies: array of different amount of deposited money
    :param rates: array of different rates of profit increase
    :param terms: number of months
    :return: void
    """
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)  # shows only from 30y to 40y of investment
    for m in monthlies:
        for r in rates:
            x, y = retire(m, r, terms)
            plt.plot(x, y,
                     label='retire '+str(m)+'$ with rate of '+str(r)+'%'
                     )
            plt.legend(loc='upper left')
    plt.show()


def displayRetireWMonthsAndRatesAndDifferentLabels(monthlies, rates, terms):
    """
    :param monthlies: array of different amount of deposited money
    :param rates: array of different rates of profit increase
    :param terms: number of months
    :return: void
    """
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)  # shows only from 30y to 40y of investment
    mLabels = ['r', 'b', 'g', 'k']
    rLabels = ['-', 'o', '--']
    for m in monthlies:
        for r in rates:
            x, y = retire(m, r, terms)
            lineStyle = mLabels[monthlies.index(m) % len(mLabels)]\
                        + rLabels[rates.index(r) % len(rLabels)]
            plt.plot(x, y,
                     lineStyle,
                     label='retire '+str(m)+'$ with rate of '+str(r)+'%'
                     )
            plt.legend(loc='upper left')
    plt.show()


# displayRetireWMonthlies([500,600,700,800,900,1000,1100], .05, 40*12)
# displayRetireWRates(900, [.04,.05,.06], 40*12)
displayRetireWMonthsAndRatesAndDifferentLabels(
    [500,700,900,1100],
    [.03,.05,.07],
    40*12
)