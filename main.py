import random
import pylab
import math
import scipy.special
import numpy

from  oneOne import *
from  oneTwo import *

from listConsts import *
from printResult import *




def printOneOne():
	printLists('listic = ',listic)
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


#Solve-------------------
# 1.1
#-------------
listic = []
genList(listic)
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
#-------------

#printOneOne()
printOneTwo()





 




# pylab.plot(teoreticDensity)
# pylab.show()

# pylab.plot(empireDensity)
# pylab.show()

# pylab.hist(listic)
# pylab.show()



# print len(listic)
# pylab.hist(listic)
# pylab.show()


