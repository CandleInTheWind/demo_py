import random
import pylab
import math
import scipy.special
import numpy


# 325 4.36 3.4  0.98 0.005

# List consts
#-----------------------
ConstOneN        = 325
ConstOneMX       = 4.36
ConstOneDX       = 3.4
ConstOneGA       = 0.98 #-0.02
ConstOneAL       = 0.005
CountOneInterval =int(1+3.32*math.log10(ConstOneN))+1



ConstTwoN = 400
ConstTwoAlpha = 0.025
ConstTwoGamma = 0.9
ConstTwoA = 0.5
ConstTwoMX = 0
ConstTwoDX = 13.1595
CountTwoInterval = int(1+3.32*math.log10(ConstTwoN)+1)