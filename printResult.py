import random
import pylab
import math
import scipy.special
import numpy 


#output data #-------------------

outfile = open("result.txt", 'w',)
outfile.close()

def printLists(structName,printLists):
    outfile = open("result.txt", 'a',)
    outfile.write(structName + '\n')
    for elem in printLists:
        outfile.write('%f\n ' %elem)
    outfile.write('\n')
    outfile.close()

# print listic print CountInterval print getStepInterval print listOfInterval
# print medianOfInterval print freqOfInterval print relativeFreqOfInterval print
# empireDensity
