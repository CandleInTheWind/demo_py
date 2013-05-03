import random
import pylab
import math
import scipy.special
import numpy 


# 325 4.36 3.4  0.98 0.005

# List consts
#-----------------------
ConstN        = 325
ConstMX       = 4.36
ConstDX       = 3.4
ConstGA       = -0.02
ConstAL       = 0.005
CountInterval =int(1+3.32*math.log10(ConstN))+1