import random
import pylab
import math
import scipy.special
import numpy

from  oneOne import *
from  oneTwo import *

from listConsts import *
from printResult import *

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

# 1.2
#--------------------
print getEmpiricalMx(listic)
print getEmpiricalDx(listic)
#--------------------






#printLists('listic = ',listic)
printLists('listOfInterval = ',listOfInterval)
printLists('medianOfInterval = ',medianOfInterval)
printLists('freqOfInterval = ',freqOfInterval)
printLists('relativeFreqOfIntervall = ',relativeFreqOfInterval)
printLists('empireDensity / Height Gists = ',empireDensity)
printLists('teoreticDensity = ', teoreticDensity)
#print empiricalMean



# pylab.plot(teoreticDensity)
# pylab.show()

# pylab.plot(empireDensity)
# pylab.show()

# pylab.hist(listic)
# pylab.show()



# print len(listic)
# pylab.hist(listic)
# pylab.show()


