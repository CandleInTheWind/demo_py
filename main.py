import random
import pylab
import math
import scipy.special

from scipy import stats

import numpy

from  oneOne import *
from  oneTwo import *
from  oneFour import *
from  oneFive import *

from listConsts import *
from printResult import *




def printOneOne(nameFile):
 	printLists(nameFile,'listic = ',listic)
	printLists(nameFile,'listOfInterval = ',listOfInterval)
	printLists(nameFile,'medianOfInterval = ',medianOfInterval)
	printLists(nameFile,'freqOfInterval = ',freqOfInterval)
	printLists(nameFile,'reblativeFreqOfIntervall = ',relativeFreqOfInterval)
	printLists(nameFile,'empireDensity / Height Gists = ',empireDensity)
	printLists(nameFile,'teoreticDensity = ', teoreticDensity)

def printOneTwo(nameFile):
	printVarible(nameFile,'EmpiricalMx = ',getEmpiricalMx(listic))
	printVarible(nameFile,'EmpiricalDx = ',getEmpiricalDx(listic))
	printVarible(nameFile,'EmpiricalMedian = ',getEmpiricalMedian(freqOfInterval,medianOfInterval))
	printVarible(nameFile,'EmpiricalDisp = '  ,getEmpiricalDisp(freqOfInterval,medianOfInterval))


def printOneFour(nameFile):
	printVarible(nameFile,'leftConfIntervalMX = ', leftConfInterval(freqOfInterval,medianOfInterval))
	printVarible(nameFile,'rightConfIntervalMX = ', rightConfInterval(freqOfInterval,medianOfInterval))
	printVarible(nameFile,'leftLimDX = ', leftLim(freqOfInterval,medianOfInterval))
	printVarible(nameFile,'rightLimDX = ', rightLim(freqOfInterval,medianOfInterval))


def printOneFive(nameFile):
	printLists(nameFile,'getProbPrac = ',getProb(getListLaplas(getListForLaplasPrac(listOfInterval,freqOfInterval,medianOfInterval))))
	printLists(nameFile,'getProbTeor = ',getProb(getListLaplas(getListForLaplasTeor(listOfInterval,freqOfInterval,medianOfInterval))))
	printVarible(nameFile,'getHiPrac = ',getHi(freqOfInterval,getListLaplas(getListForLaplasPrac(listOfInterval,freqOfInterval,medianOfInterval))))
	printVarible(nameFile,'getHiTeor = ',getHi(freqOfInterval,getListLaplas(getListForLaplasTeor(listOfInterval,freqOfInterval,medianOfInterval))))
	printVarible(nameFile,'HiAllowably = ' , getHiAllowably(len(freqOfInterval)-4,ConstOneGA))
	printVarible(nameFile,'HiAllowably = ' , getHiAllowably(len(freqOfInterval)-2,ConstOneGA))
	printNewPart()





def printAllOne(nameFile):

    printOneOne(nameFile)
    printOneTwo(nameFile)
    printOneFour(nameFile)
    printOneFive(nameFile)




def printTwoOne(nameFile):
 	printLists(nameFile,'listic = ',listic)
	printLists(nameFile,'listOfInterval = ',listOfInterval)
	printLists(nameFile,'medianOfInterval = ',medianOfInterval)
	printLists(nameFile,'freqOfInterval = ',freqOfInterval)
	printLists(nameFile,'reblativeFreqOfIntervall = ',relativeFreqOfInterval)
	printLists(nameFile,'empireDensity / Height Gists = ',empireDensity)
	printLists(nameFile,'teoreticDensity = ', teoreticDensity)

def printTwoTwo(nameFile):
	printVarible(nameFile,'EmpiricalMx = ',getTwoEmpiricalMx(listic))
	printVarible(nameFile,'EmpiricalDx = ',getTwoEmpiricalDx(listic))
	printVarible(nameFile,'EmpiricalMedian = ',getTwoEmpiricalMedian(freqOfInterval,medianOfInterval))
	printVarible(nameFile,'EmpiricalDisp = '  ,getTwoEmpiricalDisp(freqOfInterval,medianOfInterval))


def printTwoFive(nameFile):
	printLists(nameFile,'getProbPrac = ',getTwoProb(getTwoListLaplas(getTwoListForLaplasPrac(listOfInterval,freqOfInterval,medianOfInterval))))
	printLists(nameFile,'getProbTeor = ',getTwoProb(getTwoListLaplas(getTwoListForLaplasTeor(listOfInterval,freqOfInterval,medianOfInterval))))
	printVarible(nameFile,'getHiPrac = ',getTwoHi(freqOfInterval,getTwoListLaplas(getTwoListForLaplasPrac(listOfInterval,freqOfInterval,medianOfInterval))))
	printVarible(nameFile,'getHiTeor = ',getTwoHi(freqOfInterval,getTwoListLaplas(getTwoListForLaplasTeor(listOfInterval,freqOfInterval,medianOfInterval))))
	printVarible(nameFile,'HiAllowably = ' , getTwoHiAllowably(len(freqOfInterval)-4,ConstTwoGamma))
	printVarible(nameFile,'HiAllowably = ' , getTwoHiAllowably(len(freqOfInterval)-2,ConstTwoGamma))


def printAllTwo(nameFile):

    printTwoOne(nameFile)
    printTwoTwo(nameFile)
    # printTwoFour(nameFile)
    printTwoFive(nameFile)







def getListOperationOne():

    listic.sort()

    genInterals(listic,listOfInterval,freqOfInterval,medianOfInterval)

    countFreq(listic,listOfInterval,freqOfInterval)

    mergeIntervalLeftToRight(listOfInterval,freqOfInterval,medianOfInterval)
    mergeIntervalRightToLeft(listOfInterval,freqOfInterval,medianOfInterval)
    genDensity(listic,freqOfInterval,relativeFreqOfInterval,empireDensity,teoreticDensity,medianOfInterval)

def getListOperationTwo():

    listic.sort()

    genTwoInterals(listic,listOfInterval,freqOfInterval,medianOfInterval)

    countTwoFreq(listic,listOfInterval,freqOfInterval)
    mergeTwoIntervalLeftToRight(listOfInterval,freqOfInterval,medianOfInterval)
    mergeTwoIntervalRightToLeft(listOfInterval,freqOfInterval,medianOfInterval)
    genTwoDensity(listic,freqOfInterval,relativeFreqOfInterval,empireDensity,teoreticDensity,medianOfInterval)
	

#Solve-------------------
# 1.1
#-------------

for i in range (10):


	listic = genVarNormList()

	listOfInterval = []
	freqOfInterval = []
	medianOfInterval = []

	relativeFreqOfInterval = []
	empireDensity = []
	teoreticDensity = []

	getListOperationOne()

	nameFile = "Result//resultPart1-" + str(i+1)+".txt"
	outfile = open(nameFile, 'w',)
	outfile.close()
	printAllOne(nameFile)


	# PrintSection
	pylab.figure(3)
	pylab.plot(medianOfInterval,teoreticDensity)
	pylab.plot(medianOfInterval,empireDensity)
	pylab.hist(listic,bins = 10,normed = 10,histtype='bar',rwidth=1)
	pylab.savefig("Graphics//Part1-"+str(1+i) + ".png")

	pylab.close()

	#----------------------
	#2.1




	listic =  getVarHzList(genProbList())
	listic.sort()

	listOfInterval = []
	freqOfInterval = []
	medianOfInterval = []

	relativeFreqOfInterval = []
	empireDensity = []
	teoreticDensity = []

	getListOperationTwo()

	nameFile = "Result//resultPart2-" + str(i+1)+".txt"
	outfile = open(nameFile, 'w',)
	outfile.close()
	printAllTwo(nameFile)



	# # PrintSection
	pylab.figure(3)
	pylab.plot(medianOfInterval,teoreticDensity)
	pylab.plot(medianOfInterval,empireDensity)
	pylab.hist(listic,bins = 10,normed = 10,histtype='bar',rwidth=1)
	pylab.savefig("Graphics//Part2-"+str(1+i) + ".png")
	pylab.close()