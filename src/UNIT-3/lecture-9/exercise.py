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


print(getData('julyTemps.txt'))