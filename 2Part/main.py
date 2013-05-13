import random
import pylab
import math
import scipy.special
import numpy

from twoOne import *
from printResult import *
from allConsts import *


def printOneOne():
#	printLists('listic = ',listic)
	printLists('listOfInterval = ',listOfInterval)
	printLists('medianOfInterval = ',medianOfInterval)
	printLists('freqOfInterval = ',freqOfInterval)
	printLists('reblativeFreqOfIntervall = ',relativeFreqOfInterval)
	printLists('empireDensity / Height Gists = ',empireDensity)
	printLists('teoreticDensity = ', teoreticDensity)




listic =  getVaribleList(genProbList())
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

printOneOne()

pylab.plot(teoreticDensity)
#pylab.show()

pylab.plot(empireDensity)
pylab.show()

