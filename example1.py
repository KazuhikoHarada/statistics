import math
import numpy
import pylab

def getMean(data):
    sum_data = 0
    for i in data:
        sum_data += i
    return sum_data / float(len(data))

def getStandardDeviation(data, mean):
    sum_data = 0
    for i in data:
        sum_data += (i - mean)**2
        variance = sum_data / float(len(data))
    return math.sqrt(variance)

def drowHistogram(data):
    pylab.hist(data, bins = 8)
    pylab.xlabel = 'Height'
    pylab.ylabel = 'Student'
    pylab.show()

data_file = open('example1.txt', 'r')
data = []
for line in data_file:
    data.append(int(line))
data_file.close()

mean = getMean(data)
print 'mean =', mean
#print 'mean =', numpy.mean(data, axis=0)
print 'standard deviation =', getStandardDeviation(data, mean)
#print 'standard deviation =', numpy.std(data, axis=0)

drowHistogram(data)
