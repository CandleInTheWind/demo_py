import random
import pylab
import math
import scipy.special
import numpy

from  oneOne import *
from  oneTwo import *
from  oneFour import *
from  oneFive import *

from listConsts import *
from printResult import *




def printOneOne():
#	printLists('listic = ',listic)
	printLists('listOfInterval = ',listOfInterval)
	printLists('medianOfInterval = ',medianOfInterval)
	printLists('freqOfInterval = ',freqOfInterval)
	printLists('reblativeFreqOfIntervall = ',relativeFreqOfInterval)
	printLists('empireDensity / Height Gists = ',empireDensity)
	printLists('teoreticDensity = ', teoreticDensity)

def printOneTwo():
	printVarible('empiricalMx = ',getEmpiricalMx(listic))
	printVarible('EmpiricalDx = ',getEmpiricalDx(listic))
	printVarible('EmpiricalMedian = ',getEmpiricalMedian(freqOfInterval,medianOfInterval))
	printVarible('getEmpiricalDisp = ',getEmpiricalDisp(freqOfInterval,medianOfInterval))


def printOneFour():
	printVarible('leftConfInterval = ', leftConfInterval(freqOfInterval,medianOfInterval))
	printVarible('rightConfInterval = ', rightConfInterval(freqOfInterval,medianOfInterval))
	printVarible('leftLim = ', leftLim(freqOfInterval,medianOfInterval))
	printVarible('rightLim = ', rightLim(freqOfInterval,medianOfInterval))


def printOneFive():
    printLists('getProbPrac = ',getProb(getListLaplasPrac()))
    printLists('getProbTeor = ',getProb(getListLaplasTeor()))
    printVarible('getHiPrac = ',getHi(freqOfInterval,getListLaplasPrac()))
    printVarible('getHiTeor = ',getHi(freqOfInterval,getListLaplasTeor()))
    printVarible('HiAllowably = ' , 20.277739875 )

#Solve-------------------
# 1.1
#-------------
listic = []
#  genList(listic)
getList(listic)
#print len(listic)
#print listic
listic.sort()

listOfInterval = []
freqOfInterval = []
medianOfInterval = []

genInterals(listic,listOfInterval,freqOfInterval,medianOfInterval)

countFreq(listic,listOfInterval,freqOfInterval)

relativeFreqOfInterval = []
empireDensity = []
teoreticDensity = []

genDensity(listic,freqOfInterval,relativeFreqOfInterval,empireDensity,teoreticDensity,medianOfInterval)

#printOneOne()



# 1.2
printOneTwo()
#

#1.4
printOneFour()
#

#1.5
printOneFive()
#











#pylab.plot(teoreticDensity)
#pylab.show()

#pylab.plot(empireDensity)
#pylab.show()

# pylab.hist(listic)
# pylab.show()



# print len(listic)
# pylab.hist(listic)
# pylab.show()


