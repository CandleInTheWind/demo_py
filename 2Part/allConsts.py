import random
import pylab
import math
import scipy.special
import numpy

# a = 1/2,  alpha = 0.025,  Gamma = 0.9,  n = 400
#integrate x^2*1/2*e^(-1/2x)/(1+e^(-1/2x))^2   x = -1/2..1/2#
ConstN = 400
ConstAlpha = 0.025
ConstGamma = 0.9
ConstA = 0.5
ConstMX = 0
ConstDX = 0.0103197
CountInterval = int(1+3.32*math.log10(ConstN))+1
