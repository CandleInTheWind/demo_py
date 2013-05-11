import random
import pylab
import math
import scipy.special
import numpy

from listConsts import *



#--------------

def getNormDist(x):
    a       = math.sqrt(ConstDX);
    sqrtp   = math.sqrt(math.pi);
    left    = 1/(a*sqrtp)
    xminMxQ = (x- ConstMX )**2
    twoDx   = 2*ConstDX
    right   =math.e**(-(xminMxQ/twoDx))
    return left*right
#-----------------------

#-------------------
def getStepInterval(listic):
    MinInList = min(listic)
    MaxInList = max(listic)
    return (MaxInList-MinInList )/CountInterval
#-----



#-------------------
def getList(listic):
    inputText = open("input.txt",'r')
    for i in range(ConstN):
        listic.append(float(inputText.readline()))
    inputText.close()
#-----------------------------
#GEN rand num
#---
def genList(listic):
    for i in range(ConstN):
        listic.append(random.normalvariate(ConstMX,math.sqrt(ConstDX)))
#---

#len of equal interval
#------
def genInterals(listic,listOfInterval,freqOfInterval,medianOfInterval):
    cur = min(listic)
    for i in range(CountInterval+1):
        listOfInterval.append(cur)
        freqOfInterval.append(0)
        medianOfInterval.append(( cur + (cur + getStepInterval(listic)))/2)
        cur = cur + getStepInterval(listic)
    del(medianOfInterval[len(medianOfInterval)-1])
    del(freqOfInterval[len(freqOfInterval)-1])
#-----

#countFreq
#------------------------
def countFreq(listic,listOfInterval,freqOfInterval):
    ind = 0
    i = 0
    while i <len(listic) and ind < len(listOfInterval)-1:
        elem = listic[i]
        if elem >=listOfInterval[ind] and elem < listOfInterval[ind+1]:
            freqOfInterval[ind] = freqOfInterval[ind] + 1
            i = i + 1
        else: ind = ind + 1
    freqOfInterval[len(freqOfInterval)-1] = freqOfInterval[len(freqOfInterval)-1] + 1
#------------------------

#------------------------
def genDensity(listic,freqOfInterval,relativeFreqOfInterval,empireDensity,teoreticDensity,medianOfInterval):
    i = 0
    for elem in freqOfInterval:
        relativeFreqOfInterval.append((elem/(ConstN+0.0)))
        empireDensity.append((elem/(ConstN+0.0))/getStepInterval(listic))
        teoreticDensity.append(getNormDist(medianOfInterval[i]))
        i = i +1
#------------------------
