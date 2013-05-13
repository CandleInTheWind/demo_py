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

def printVarible(varName,var):
	outfile = open("result.txt", 'a',)
	outfile.write(varName)
	outfile.write('%f\n ' %var)
	outfile.write('\n')
	outfile.close()

 
