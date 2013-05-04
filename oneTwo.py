import random
import pylab
import math
import scipy.special
import numpy 

from listConsts import *
from oneOne import *
#-----
def getEmpiricalMx(listic):
    empiricalMean = 0
    for elem in listic:
        empiricalMean = empiricalMean + elem
    empiricalMean = empiricalMean/(ConstN+0.0)
    return empiricalMean
#----

#----

# Does not work
def getEmpiricalDx(listic):
    empiricalDx = 0
    for elem in listic:
        empiricalDx = empiricalDx + (getEmpiricalMx(listic) - elem) ** 2
    empiricalDx = (empiricalDx/(ConstN+0.0))
    return empiricalDx
#----


#----
def getEmpiricalMedian(freqOfInterval,medianOfInterval):
    sum = 0
    for i in range(CountInterval):
        sum = sum + freqOfInterval[i] * medianOfInterval[i]
    sum = sum / ConstN
    return sum

def getEmpiricalDisp(freqOfInterval,medianOfInterval):
    sum = 0
    median = getEmpiricalMedian(freqOfInterval,medianOfInterval)
    for i in range(CountInterval):
        sum = sum + freqOfInterval[i] * (medianOfInterval[i] - median)**2
    sum = sum / ConstN
    return sum



