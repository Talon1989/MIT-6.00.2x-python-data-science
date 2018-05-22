import pylab

sample = []
quadratic = []
threeXplus2 = []
for i in range(6):
    sample.append(i)
    quadratic.append(i**2)
    threeXplus2.append(3*i + 2)

pylab.plot(sample, label='linear')
pylab.plot(quadratic, label='quadratic')
# pylab.yscale('symlog')
pylab.legend()
pylab.ylabel('output')
pylab.show()

print(pylab.polyfit(sample, threeXplus2, 1))