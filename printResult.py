import random
import pylab
import math
import scipy.special
import numpy 


#output data #-------------------



def printLists(nameFile,structName,printLists):
    outfile = open(nameFile, 'a',)
    outfile.write(structName + '\n')
    for elem in printLists:
        outfile.write('%f\n ' %elem)
    outfile.write('\n')
    outfile.close()

def printVarible(nameFile,varName,var):
	outfile = open(nameFile, 'a',)
	outfile.write(varName)
	outfile.write('%f\n ' %var)
	outfile.write('\n')
	outfile.close()

def printNewPart():
    outfile = open("result.txt", 'a',)
    outfile.write("============= \n NewPart \n===============\n")

 
