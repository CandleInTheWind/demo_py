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
        newList.append((elem  - ConstMX)/math.sqrt(getEmpiricalDisp(freqOfInterval,medianOfInterval)))
    return newList


#[-2.725822255065761, -2.2337965772560566, -1.7417708994463528,
# -1.2497452216366485, -0.7577195438269443, -0.2656938660172402,
# 0.22633181179246378, 0.7183574896021678,
#1.2103831674118717, 1.7024088452215758, 2.1944345230312803]

def getListLaplasPrac():
    temp = [0.0032070789,0.0127482165,0.0407742615,0.1056963566,0.2243093117,0.3952374423,0.5895283942,0.7637314035,0.886934019,0.955660638,0.985897924]
    return temp
def getListLaplasTeor():
    temp =[0.00268442,0.0109527639,0.035932214,0.0954449648,0.2072715163,0.3730072505,0.5667579223,0.7454218542,0.875376032,0.9499329645,0.9836696236]
    return temp
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
       sum = sum + ((freqOfInterval[i] - ConstN*temp[i])**2)/(ConstN*temp[i])
    return sum

