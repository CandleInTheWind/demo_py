import random
import pylab
import math
import scipy.special
import numpy

from listConsts import *
from oneOne import *
from oneTwo import *


def getListForLaplasPrac(listOfInterval,freqOfInterval,medianOfInterval):
    newList = []
    for elem in listOfInterval:
        newList.append((elem  - getEmpiricalMedian(freqOfInterval,medianOfInterval))/math.sqrt(getEmpiricalDisp(freqOfInterval,medianOfInterval)))
    return newList

def getListForLaplasTeor(listOfInterval,freqOfInterval,medianOfInterval):
    newList = []
    for elem in listOfInterval:
        newList.append((elem  - ConstOneMX)/math.sqrt(getEmpiricalDisp(freqOfInterval,medianOfInterval)))
    return newList


def getListLaplas(temp):
    return map(lambda x : 0.5*math.erfc(-x/math.sqrt(2)),temp)


def getProb(temp):
    newList = []
    for i in range(len(temp)-1):
        newList.append(temp[i+1]-temp[i])
    return newList


def getHi(freqOfInterval,typeListLaplas):
    sum = 0
    sumFreq = 0
    temp = getProb(typeListLaplas)
    for i in range(len(temp)):
       sum = sum + ((freqOfInterval[i] - ConstOneN*temp[i])**2)/(ConstOneN*temp[i])
    return sum



def getHiAllowably(ind,gamma):
    if gamma == ConstTwoGamma:
        temp = [2.706 ,4.605 ,6.251 ,7.779 ,9.236 ,10.645,12.017,13.362,14.684,15.987,17.275,18.549,19.12,21.064,22.307,23.542,24.769,25.989,27.204,28.412,29.615,30.813,32.007,33.196,34.382,35.563,36.741,37.916,39.087,40.256]
    else: temp = [7.879 ,10.597,12.838,14.860,16.750,18.548,20.278,21.955,23.589,25.188,26.757,28.300,29.819,31.319,32.801,34.267,35.718,37.156,38.582,39.997,41.401,42.796,44.181,45.558,46.928,48.290,49.645,50.993,52.336,53.672]
    return temp[ind]



#-------------------------------------------------------------


def getTwoListForLaplasPrac(listOfInterval,freqOfInterval,medianOfInterval):
    newList = []
    for elem in listOfInterval:
        newList.append((elem  - getTwoEmpiricalMedian(freqOfInterval,medianOfInterval))/math.sqrt(getTwoEmpiricalDisp(freqOfInterval,medianOfInterval)))
    return newList

def getTwoListForLaplasTeor(listOfInterval,freqOfInterval,medianOfInterval):
    newList = []
    for elem in listOfInterval:
        newList.append((elem  - ConstTwoMX)/math.sqrt(getTwoEmpiricalDisp(freqOfInterval,medianOfInterval)))
    return newList


def getTwoListLaplas(temp):
    return map(lambda x : 0.5*math.erfc(-x/math.sqrt(2)),temp)


def getTwoProb(temp):
    newList = []
    for i in range(len(temp)-1):
        newList.append(temp[i+1]-temp[i])
    return newList


def getTwoHi(freqOfInterval,typeListLaplas):
    sum = 0
    sumFreq = 0
    temp = getTwoProb(typeListLaplas)
    for i in range(len(temp)):
       sum = sum + ((freqOfInterval[i] - ConstTwoN*temp[i])**2)/(ConstTwoN*temp[i])
    return sum



def getTwoHiAllowably(ind,gamma):
    if gamma == ConstTwoGamma:
        temp = [2.706 ,4.605 ,6.251 ,7.779 ,9.236 ,10.645,12.017,13.362,14.684,15.987,17.275,18.549,19.12,21.064,22.307,23.542,24.769,25.989,27.204,28.412,29.615,30.813,32.007,33.196,34.382,35.563,36.741,37.916,39.087,40.256]
    else: temp = [7.879 ,10.597,12.838,14.860,16.750,18.548,20.278,21.955,23.589,25.188,26.757,28.300,29.819,31.319,32.801,34.267,35.718,37.156,38.582,39.997,41.401,42.796,44.181,45.558,46.928,48.290,49.645,50.993,52.336,53.672]
    return temp[ind]