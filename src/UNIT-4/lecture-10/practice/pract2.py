import pylab


sample = []
linear = []
quadratic = []

for n in range(10):
    sample.append(n)
    linear.append(3*n + 2)
    quadratic.append(n ** 2)


sample = pylab.array(sample)
linear = pylab.array(linear)
quadratic = pylab.array(quadratic)

print(pylab.polyfit(sample, linear, 1))