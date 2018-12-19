import numpy
import scipy
import matplotlib.pyplot as plt
import os

numpy.set_printoptions(threshold=numpy.inf, linewidth=numpy.inf)
setPath = '../assets/barker13.sc'

dir = os.path.dirname(__file__)
filename = os.path.join(dir, setPath)

dataComplex = numpy.fromfile(filename, dtype='int16')
dataSize = numpy.size(dataComplex)

class Barker(object):
  sequence = []
  timeLength = 0;
  time = []
  sequenceRepeated = []
  title = ""
  
  def __init__(self, sequence, time, timeLength, title):
    self.sequence = sequence
    self.time = time
    self.timeLength = timeLength
    self.title = title
    self.sequenceRepeated = numpy.repeat(sequence,10)


Barker7 = Barker(numpy.array([1, 1, 1, -1, -1, 1, -1,0,0,0]), numpy.linspace(0,10,num=100), 10, '7 Sequence Barker Code')
Barker13 = Barker(numpy.array([1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,0,0,0,0,0,0,0]), numpy.linspace(0,20,num=200), 20, '13 Sequence Barker Code')

plt.plot(Barker7.time,Barker7.sequenceRepeated)
plt.title(Barker7.title)
plt.xlabel('micro-seconds')
plt.ylabel('Signal Strength')
plt.show()

plt.plot(Barker13.time,Barker13.sequenceRepeated)
plt.title(Barker13.title)
plt.xlabel('micro-seconds')
plt.ylabel('Signal Strength')
plt.show()

def BarkerAutoCorrelation(signal):
  autoCorr = numpy.correlate(signal.sequenceRepeated, signal.sequenceRepeated, mode='full')
  timeSpace = numpy.linspace(-signal.timeLength,signal.timeLength,num=len(signal.sequenceRepeated)*2-1)
  plt.plot(timeSpace,autoCorr)
  plt.xlabel('micro-seconds')
  plt.ylabel('Signal Strength')
  plt.title('Auto-Correlation of ' + signal.title)
  plt.show()
  return autoCorr

BarkerAutoCorrelation(Barker7)
BarkerAutoCorrelation(Barker13)