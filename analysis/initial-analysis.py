import numpy

data_frame = numpy.genfromtxt('../data/runs.csv', delimiter=',', dtype=None, names=True)
print(dir(data_frame))
