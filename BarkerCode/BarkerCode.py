import numpy
import scipy
import matplotlib.pyplot as plot
import os

numpy.set_printoptions(threshold=numpy.inf, linewidth=numpy.inf)
setPath = '../assets/barker13.sc'

dir = os.path.dirname(__file__)
filename = os.path.join(dir, setPath)

dataComplex = numpy.fromfile(filename, dtype='int16')
print(dataComplex)

dataSize = numpy.size(dataComplex)

print(dataSize)
