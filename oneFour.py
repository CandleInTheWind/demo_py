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



#--------------------------------------

cPlusY = 1.65 # (1+ConstTwoGamma)/2



def getTwoSqrtEmpDisp(freqOfInterval,medianOfInterval):
    return math.sqrt(getTwoEmpiricalDisp(freqOfInterval,medianOfInterval))

 
# Confidence_interval
def leftTwoConfInterval(freqOfInterval,medianOfInterval):
    medA = getTwoEmpiricalMedian(freqOfInterval,medianOfInterval) 
    sqrtDistDivSqrtN = getTwoSqrtEmpDisp(freqOfInterval,medianOfInterval) / math.sqrt(ConstTwoN)
    return medA - cPlusY*sqrtDistDivSqrtN
     
def rightTwoConfInterval(freqOfInterval,medianOfInterval):
    medA = getTwoEmpiricalMedian(freqOfInterval,medianOfInterval) 
    sqrtDistDivSqrtN = getTwoSqrtEmpDisp(freqOfInterval,medianOfInterval) / math.sqrt(ConstTwoN)
    return medA + cPlusY*sqrtDistDivSqrtN
#---------------------


def getM4(listic,freqOfInterval,medianOfInterval):
    sum = 0
    med = getTwoEmpiricalMedian(freqOfInterval,medianOfInterval)
    for elem in listic:
        sum = sum + (elem-med)**4
    sum = sum / ConstTwoN
    return sum


def someTempCalc(listic,freqOfInterval,medianOfInterval):
    M4 = getM4(listic,freqOfInterval,medianOfInterval)
    disp = getTwoEmpiricalDisp(freqOfInterval,medianOfInterval)
    disp = disp**2

    return math.sqrt((M4-disp)/ConstTwoN)

def leftTwoLim(listic,freqOfInterval,medianOfInterval):
    temp = someTempCalc(listic,freqOfInterval,medianOfInterval)
    disp = getTwoEmpiricalDisp(freqOfInterval,medianOfInterval)
    return disp - temp*cPlusY


    
def rightTwoLim(listic,freqOfInterval,medianOfInterval):
    temp = someTempCalc(listic,freqOfInterval,medianOfInterval)
    disp = getTwoEmpiricalDisp(freqOfInterval,medianOfInterval)
    return disp + temp*cPlusY