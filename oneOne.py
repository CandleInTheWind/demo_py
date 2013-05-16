import random
import pylab
import math
import scipy.special
import numpy

from listConsts import *



#--------------

def getNormDist(x):
    a       = math.sqrt(ConstOneDX );
    sqrtp   = math.sqrt(math.pi);
    left    = 1/(a*sqrtp)
    xminMxQ = (x- ConstOneMX  )**2
    twoDx   = 2*ConstOneDX 
    right   =math.e**(-(xminMxQ/twoDx))
    return left*right
#-----------------------

#-------------------
def getStepInterval(listic):
    MinInList = min(listic)
    MaxInList = max(listic)
    return (MaxInList-MinInList )/CountOneInterval
#-----



#-------------------
def getList():
    listic = []
    inputText = open("input.txt",'r')
    for i in range(ConstOneN):
        listic.append(float(inputText.readline()))
    inputText.close()
    return listic
#-----------------------------
#GEN rand num
#---
def genVarNormList():
    listic = []
    for i in range(ConstOneN):
        listic.append(random.normalvariate(ConstOneMX ,math.sqrt(ConstOneDX )))
    return listic
#---

#len of equal interval
#------
def genInterals(listic,listOfInterval,freqOfInterval,medianOfInterval):
    cur = min(listic)
    for i in range(CountOneInterval+1):
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
    if sum(freqOfInterval)!=ConstOneN:
        freqOfInterval[len(freqOfInterval)-1] = freqOfInterval[len(freqOfInterval)-1] + 1
#------------------------




def mergeIntervalLeftToRight(listOfInterval,freqOfInterval,medianOfInterval):
    i  =  0
    while i < (len(freqOfInterval)-2):
        if (freqOfInterval[i] < 5):
            freqOfInterval[i+1] = freqOfInterval[i] + freqOfInterval[i+1]
            medianOfInterval[i] = (listOfInterval[i] + 0.0 + listOfInterval[i+2])/2
            del (freqOfInterval[i])
            del (listOfInterval[i+1])
            del (medianOfInterval[i+1])
        else: 
            i = i + 1

def mergeIntervalRightToLeft(listOfInterval,freqOfInterval,medianOfInterval):
    listOfInterval.reverse()
    freqOfInterval.reverse()
    medianOfInterval.reverse()
    mergeIntervalLeftToRight(listOfInterval,freqOfInterval,medianOfInterval)
    listOfInterval.reverse()
    freqOfInterval.reverse()
    medianOfInterval.reverse()

#------------------------
def genDensity(listic,freqOfInterval,relativeFreqOfInterval,empireDensity,teoreticDensity,medianOfInterval):
    i = 0
    for elem in freqOfInterval:
        relativeFreqOfInterval.append((elem/(ConstOneN+0.0)))
        empireDensity.append((elem/(ConstOneN+0.0))/getStepInterval(listic))
        teoreticDensity.append(getNormDist(medianOfInterval[i]))
        i = i +1
#------------------------

#2.1------------------------------------



def getBasicFunc(x):
    chis = ConstTwoA *math.e**(-ConstTwoA*x)
    znam = (1+math.e**(-ConstTwoA*x))**2
    return chis/znam

def getVarHzList(listic):
    return map(lambda y : -2*math.log(math.fabs(1/y + -1)),listic)


def genProbList():
    listic = []
    for i in range(ConstTwoN):
        listic.append(random.random())
    return listic



def getStepTwoInterval(listic):
    MinInList = min(listic)
    MaxInList = max(listic)
    return (MaxInList-MinInList )/CountTwoInterval


#len of equal interval
#------
def genTwoInterals(listic,listOfInterval,freqOfInterval,medianOfInterval):
    cur = min(listic)
    for i in range(CountTwoInterval +1):
        listOfInterval.append(cur)
        freqOfInterval.append(0)
        medianOfInterval.append(( cur + (cur + getStepTwoInterval(listic)))/2)
        cur = cur + getStepTwoInterval(listic)
    del(medianOfInterval[len(medianOfInterval)-1])
    del(freqOfInterval[len(freqOfInterval)-1])
#-----

#countFreq
#------------------------
def countTwoFreq(listic,listOfInterval,freqOfInterval):
    ind = 0
    i = 0
    while i <len(listic) and ind < len(listOfInterval)-1:
        elem = listic[i]
        if elem >=listOfInterval[ind] and elem < listOfInterval[ind+1]:
            freqOfInterval[ind] = freqOfInterval[ind] + 1
            i = i + 1
        else: ind = ind + 1
    if sum(freqOfInterval)!=ConstTwoN:
        freqOfInterval[len(freqOfInterval)-1] = freqOfInterval[len(freqOfInterval)-1] + 1
#------------------------




def mergeTwoIntervalLeftToRight(listOfInterval,freqOfInterval,medianOfInterval):
    i  =  0
    while i < (len(freqOfInterval)-2):
        if (freqOfInterval[i] < 5):
            freqOfInterval[i+1] = freqOfInterval[i] + freqOfInterval[i+1]
            medianOfInterval[i] = (listOfInterval[i] + 0.0 + listOfInterval[i+2])/2
            del (freqOfInterval[i])
            del (listOfInterval[i+1])
            del (medianOfInterval[i+1])
        else: 
            i = i + 1

def mergeTwoIntervalRightToLeft(listOfInterval,freqOfInterval,medianOfInterval):
    listOfInterval.reverse()
    freqOfInterval.reverse()
    medianOfInterval.reverse()
    mergeTwoIntervalLeftToRight(listOfInterval,freqOfInterval,medianOfInterval)
    listOfInterval.reverse()
    freqOfInterval.reverse()
    medianOfInterval.reverse()





#------------------------
def genTwoDensity(listic,freqOfInterval,relativeFreqOfInterval,empireDensity,teoreticDensity,medianOfInterval):
    i = 0
    for elem in freqOfInterval:
        relativeFreqOfInterval.append((elem/(ConstTwoN+0.0)))
        empireDensity.append((elem/(ConstTwoN+0.0))/getStepTwoInterval(listic))
        teoreticDensity.append(getBasicFunc(medianOfInterval[i]))
        i = i +1
#------------------------
