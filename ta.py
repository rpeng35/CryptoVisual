import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('15min.csv', delimiter = ',')

print(my_data)

close = my_data[:,4]
print(close)

#close = numpy.random.random(100)

#moving_average = talib.SMA(close)

#print(moving_average)

rsi = talib.RSI(close)
print(rsi)