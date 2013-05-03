import random
import pylab
import math
import scipy.special

# txt = open('results10.txt','w',)
#  325 4.36 3.4  0.98 0.005

# List consts
#-----------------------
ConstN        = 325
ConstMX       = 4.36
ConstDX       = 3.4
ConstGA       = -0.02
ConstAL       = 0.005
CountInterval = int(1+3.32*math.log10(ConstN))+1
#-----------------------
#GEN rand num
#----
listic = []
for i in range(ConstN):
	listic.append(random.normalvariate(ConstMX,math.sqrt(ConstDX)));
#---

MinInList = min(listic)
MaxInList = max(listic)

#len of equal interval
#------
stepInterval = ( -MinInList + MaxInList)/CountInterval
#-----

listOfInterval = []
frequencyOfInterval = []
medianOfInterval = []

sizeOfInterval = CountInterval+1





#gen list otr
#------
cur = MinInList
for i in range(sizeOfInterval):
	listOfInterval.append(cur)
	frequencyOfInterval.append(0)
	medianOfInterval.append(( cur + (cur + stepInterval))/2)
	cur = cur + stepInterval
cur = 0
#-----

del(medianOfInterval[len(medianOfInterval)-1])
del(frequencyOfInterval[len(frequencyOfInterval)-1])


listic.sort()

print len(listic)

ind = 0
i = 0
while i < len(listic) and ind < len(listOfInterval)-1:
	elem = listic[i]
	if elem >= listOfInterval[ind] and elem < listOfInterval[ind+1]:
		frequencyOfInterval[ind] = frequencyOfInterval[ind] + 1
		i = i + 1
	else:
		ind = ind + 1

frequencyOfInterval[len(frequencyOfInterval)-1] = frequencyOfInterval[len(frequencyOfInterval)-1] + 1

relativeFreOfInterval = []
empireDensity = []
for elem in frequencyOfInterval:
	relativeFreOfInterval.append((elem/(ConstN+0.0)))
	empireDensity.append((elem/(ConstN+0.0))/stepInterval)





# print listic
# print CountInterval
# print stepInterval
# print listOfInterval
# print medianOfInterval
# print frequencyOfInterval
# print relativeFreOfInterval
# print empireDensity

def OLOLO(structName,ololo):
    outfile = open("OLOLO.txt", 'a',)
    outfile.write(structName)
    for elem in ololo:
		outfile.write('%f, ' % elem)
    outfile.write('\n')
    outfile.close()

outfile = open("OLOLO.txt", 'w',)
outfile.close()

OLOLO('listic = ',listic)
OLOLO('listOfInterval = ',listOfInterval)
OLOLO('medianOfInterval = ',medianOfInterval)
OLOLO('frequencyOfInterval = ',frequencyOfInterval)
OLOLO('relativeFreOfIntervall = ',relativeFreOfInterval)
OLOLO('empireDensity / Height Gists = ',empireDensity)



#print len(listic)
# pylab.hist(listic)
# pylab.show()


