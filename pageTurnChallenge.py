#!/bin/python

import sys


n = int(raw_input().strip())
p = int(raw_input().strip())
# your code goes here
fromStart=p/2
if n%2==0:
    n+=1
fromEnd=(n-p)/2
print min(fromStart,fromEnd)