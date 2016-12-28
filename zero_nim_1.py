import sys

def findNoOfNonZeroEntries(p):
    count=0
    for each in p:
        if each>0:
            count+=1
    return count

def reduceIteratively(p,Min):
    new_p=[]
    for each in p:
        new_p.append(each-Min)
    return new_p

def removeZeros(p):
    new_p=[]
    for each in p:
        if each!=0:
            new_p.append(each)
    return new_p

g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    p = map(int,raw_input().strip().split(' '))
    # your code goes here
    while(1):
        noOfZeroes=findNoOfNonZeroEntries(p)
        if noOfZeroes==1:
            if n%2==0:
                print 'W'
            else:
                print 'L'
            break
        elif noOfZeroes==0:
            if n%2==1:
                print 'W'
            else:
                print 'L'
            break
        else:
            MinVal=min(p)
            p=reduceIteratively(p,MinVal)
            p=removeZeros(p)