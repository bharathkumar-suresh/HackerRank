#!/bin/python

import sys
import math

n,p = raw_input().strip().split(' ')
n,p = [int(n),int(p)]
a = map(int,raw_input().strip().split(' '))
# your code goes here
maxVal=-1
finalVal=0.0
numbersPresent={}
a=sorted(a)
for each in a:
    val=math.ceil(float(each)/p)
    if not numbersPresent.has_key(val):
        if val>maxVal:
            maxVal=val
        numbersPresent[val]=1
        finalVal+=val
    else:
        maxVal+=1.0
        finalVal+=maxVal
        numbersPresent[maxVal]=1
print int(finalVal)
