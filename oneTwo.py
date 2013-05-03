import random
import pylab
import math
import scipy.special
import numpy 

from listConsts import *

#-----
def getEmpiricalMx(listic):
    empiricalMean = 0
    for elem in listic:
        empiricalMean = empiricalMean + elem
    empiricalMean = empiricalMean/(ConstN+0.0)
    return empiricalMean
#----

#----

# Does not work
def getEmpiricalDx(listic):
    empiricalDx = 0
    for elem in listic:
        empiricalDx = empiricalDx + elem*elem
    empiricalDx = (empiricalDx/(ConstN+0.0))
    emp = 0
    for elem in listic:
        emp = emp + elem*elem
    emp = (emp/(ConstN+0.0))
    emp = emp**2
    empiricalDx = empiricalDx - emp
    return empiricalDx
#----