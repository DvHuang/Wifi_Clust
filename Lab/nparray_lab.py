import numpy

b = numpy.arange(16).reshape(4,4)
print b
print b[::2, ::2]
print b[1::2, ::2]
print b[::2, 1::2]
print b[1::2, 1::2]
b = b[::2, ::2] + b[1::2, ::2] + b[::2, 1::2] + b[1::2, 1::2]
print ("b=",b)
