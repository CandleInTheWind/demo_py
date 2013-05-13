import random
import pylab
import math
import scipy.special
import numpy

from allConsts import *

def getBasicFunc(x):
    chis = ConstA*math.e**(-ConstA*x)
    znam = (1+math.e**(-ConstA*x))**2
    return chis/znam

def getVaribleList(listic):
    return map(lambda y : -2*math.log(math.fabs(1/y + -1)),listic)


def genProbList():
    listic = []
    for i in range(ConstN):
        listic.append(random.random())
    return listic

def getStepInterval(listic):
    MinInList = min(listic)
    MaxInList = max(listic)
    return (MaxInList-MinInList )/CountInterval


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
        teoreticDensity.append(getBasicFunc(medianOfInterval[i]))
        i = i +1
#------------------------
