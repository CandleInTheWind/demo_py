import random
import pylab
import math
import scipy.special
import numpy

from listConsts import *
from oneOne import *
from oneTwo import *


levelKvan    = (ConstOneGA + 1)/2
kvanStudenta = 2.326
leftKvan     = levelKvan
rightKvan    = (1 - ConstOneGA ) / 2


def getSqrtEmpDisp(freqOfInterval,medianOfInterval):
    return math.sqrt(getEmpiricalDisp(freqOfInterval,medianOfInterval))

def countMidLenInter(freqOfInterval,medianOfInterval):
    temp =  getSqrtEmpDisp(freqOfInterval,medianOfInterval)
    return  temp/math.sqrt(ConstOneN-1) * kvanStudenta

# Confidence_interval
def leftConfInterval(freqOfInterval,medianOfInterval):
    midLenInter = countMidLenInter(freqOfInterval,medianOfInterval)
    return getEmpiricalMedian(freqOfInterval,medianOfInterval) - midLenInter
def rightConfInterval(freqOfInterval,medianOfInterval):
    midLenInter = countMidLenInter(freqOfInterval,medianOfInterval)
    return getEmpiricalMedian(freqOfInterval,medianOfInterval) + midLenInter
#---------------------


def correctEmpDisp(freqOfInterval,medianOfInterval):
    return ((ConstOneN+0.0)/(ConstOneN-1)) * getEmpiricalDisp(freqOfInterval,medianOfInterval)

def levKvantLeft():
    return ((kvanStudenta + math.sqrt(2*ConstOneN-1))**2)/2
def levKvantRight():
    return ((-kvanStudenta + math.sqrt(2*ConstOneN-1))**2)/2
# leftGran
def leftLim(freqOfInterval,medianOfInterval):
    return correctEmpDisp(freqOfInterval,medianOfInterval)*(ConstOneN - 1)/(levKvantLeft())
    
def rightLim(freqOfInterval,medianOfInterval):
    return correctEmpDisp(freqOfInterval,medianOfInterval)*(ConstOneN - 1)/(levKvantRight())
