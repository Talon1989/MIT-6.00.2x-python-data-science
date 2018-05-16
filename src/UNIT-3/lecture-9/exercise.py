import pylab


def getStd(data):
    mean = sum(data) / len(data)
    tot = 0.0
    for d in data:
        tot = (d-mean) ** 2
    return (tot / mean) ** 0.5

def getData(file):
    inFile = open(str(file))
    lowTemps = []
    highTemps = []
    for l in inFile:
        line = l.split()
        if len(line) != 3 or 'Boston' == line[0] or 'Day' == line[0]:
            continue
        else:
            highTemps.append(int(line[1]))
            lowTemps.append(int(line[2]))
    return lowTemps, highTemps



lTemps, hTemps = getData('julyTemps.txt')
pylab.errorbar([n for n in range(len(lTemps))], lTemps
                , yerr=1.96*pylab.array(getStd(lTemps))
                , label='95% Confidence Interval')
pylab.show()

