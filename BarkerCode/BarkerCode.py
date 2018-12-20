import numpy
import scipy
import matplotlib.pyplot as plt
import os

numpy.set_printoptions(threshold=numpy.inf, linewidth=numpy.inf)
setPath = '../assets/barker13.sc'

dir = os.path.dirname(__file__)
filename = os.path.join(dir, setPath)

dataComplex = numpy.fromfile(filename, dtype='int16')
dataComplex = 1.0*dataComplex[::2]+1.0j*dataComplex[1::2]
print(dataComplex)
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
plt.ylabel('Amplitude')
plt.xticks(numpy.linspace(0,10,11))
plt.show()

plt.plot(Barker13.time,Barker13.sequenceRepeated)
plt.title(Barker13.title)
plt.xlabel('micro-seconds')
plt.ylabel('Amplitude')
plt.xticks(numpy.linspace(0,20,21))
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

def PlotSignalStrength(data):
  dataStrength = numpy.square(numpy.abs(data))
  plt.title('Signal Strength of Returning Objects w/o Correlation')
  plt.xlabel('Range: x150m')
  plt.ylabel('Signal Strength')
  plt.xlim([0,63])
  plt.xticks(numpy.linspace(0,63,22))
  plt.plot(dataStrength)
  plt.show()
  return

def SignalStrengthBarker(signal, data):
  dataStrength = numpy.square(numpy.abs(data))
  autoCorr = numpy.correlate(data, Barker13.sequence, mode='same')
  plt.plot(abs(autoCorr)**2)
  plt.title('Signal Strength of Returning Objects w/ Barker13 Correlation')
  plt.xlabel('Range')
  plt.ylabel('Signal Strength')
  plt.show()
  return


BarkerAutoCorrelation(Barker7)
BarkerAutoCorrelation(Barker13)

PlotSignalStrength(dataComplex)
SignalStrengthBarker(Barker13, dataComplex)

