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
    empiricalMean = empiricalMean/(ConstOneN+0.0)
    return empiricalMean
#----

#----

def getEmpiricalDx(listic):
    empiricalDx = 0
    for elem in listic:
        empiricalDx = empiricalDx + (getEmpiricalMx(listic) - elem) ** 2
    empiricalDx = (empiricalDx/(ConstOneN+0.0))
    return empiricalDx
#----


#----
def getEmpiricalMedian(freqOfInterval,medianOfInterval):
    sum = 0
    for i in range (len(freqOfInterval)):
        sum = sum + freqOfInterval[i] * medianOfInterval[i]
    sum = sum / ConstOneN
    return sum

def getEmpiricalDisp(freqOfInterval,medianOfInterval):
    sum = 0
    median = getEmpiricalMedian(freqOfInterval,medianOfInterval)
    for i in range (len(freqOfInterval)):
        sum = sum + freqOfInterval[i] * (medianOfInterval[i] - median)**2
    sum = sum / ConstOneN
    return sum

#---------------------------------------------------------


def getTwoEmpiricalMx(listic):
    empiricalMean = 0
    for elem in listic:
        empiricalMean = empiricalMean + elem
    empiricalMean = empiricalMean/(ConstTwoN+0.0)
    return empiricalMean
#----

#----

def getTwoEmpiricalDx(listic):
    empiricalDx = 0
    for elem in listic:
        empiricalDx = empiricalDx + (getTwoEmpiricalMx(listic) - elem) ** 2
    empiricalDx = (empiricalDx/(ConstTwoN+0.0))
    return empiricalDx
#----


#----
def getTwoEmpiricalMedian(freqOfInterval,medianOfInterval):
    sum = 0
    for i in range (len(freqOfInterval)):
        sum = sum + freqOfInterval[i] * medianOfInterval[i]
    sum = sum / ConstTwoN
    return sum

def getTwoEmpiricalDisp(freqOfInterval,medianOfInterval):
    sum = 0
    median = getTwoEmpiricalMedian(freqOfInterval,medianOfInterval)
    for i in range (len(freqOfInterval)):
        sum = sum + freqOfInterval[i] * (medianOfInterval[i] - median)**2
    sum = sum / ConstTwoN
    return sum



