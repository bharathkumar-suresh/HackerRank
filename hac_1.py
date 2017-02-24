#!/bin/python

import sys

matrixMultiplyMatrix=[[1,2,3],[1,0,0],[0,1,0]]
intitialMatrix=[3,2,1]
hackonacciSequence=[1,2,3]

n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]

hackonacciStoredValues={}

def multiplyMatrices(A,B): #Multiply 3by3 matrices
    productMatrix=[[0,0,0],[0,0,0],[0,0,0]]
    #print A,B
    for i in range(0,len(A)):
        for j in range(0,len(A[i])):
            for k in range(0,len(B)):
                productMatrix[i][k]+=A[i][j]*B[j][k]
    for i in range(0,3):
        for j in range(0,3):
            productMatrix[i][j]=productMatrix[i][j]%2
    return productMatrix


    #return np.dot(A,B)

def NPowerMatrixMultiply(n):
    if n==1:
        return matrixMultiplyMatrix
    if hackonacciStoredValues.has_key(n):
        return hackonacciStoredValues[n]
    if n%2==0:
        tempMatrix=NPowerMatrixMultiply(n/2)
        V= multiplyMatrices(tempMatrix,tempMatrix)
        hackonacciStoredValues[n]=V
        return V
    if n%2==1:
        tempMatrix=NPowerMatrixMultiply(n/2)
        V= multiplyMatrices(multiplyMatrices(tempMatrix,tempMatrix),matrixMultiplyMatrix)
        hackonacciStoredValues[n]=V
        return V

def findNthElement(n):
    if n<=3:
        return hackonacciSequence[n-1]
    multipliedMatrix=NPowerMatrixMultiply(n-3)
    return 3*multipliedMatrix[0][0]+2*multipliedMatrix[0][1]+multipliedMatrix[0][2]

H=[]
for i in range(0,n):
    H.append([])
    for j in range(0,n):
        H[i].append('')
for i in range(0,n):
    for j in range(i,n):
        product=((i+1)*(j+1))**2
        H[i][j]=findNthElement(product)
        if H[i][j]%2==0:
            H[i][j]='X'
        else:
            H[i][j]='Y'
        H[j][i]=H[i][j]
#print H

def rotateBy90(H):
    newH=[]
    for i in range(0,n):
        newH.append([])
        for j in range(0,n):
            newH[i].append(0)
    for i in range(0,n):
        for j in range(0,n):
            newH[j][n-i-1]=H[i][j]
    return newH

def findDifference(H,newH):
    count=0
    for i in range(0,n):
        for j in range(0,n):
            if H[i][j]!=newH[i][j]:
                count+=1
    return count

newH_90=rotateBy90(H)
newH_180=rotateBy90(newH_90)
newH_270=rotateBy90(newH_180)
changes=[0,0,0,0]
changes[1]=findDifference(H,newH_90)
changes[2]=findDifference(H,newH_180)
changes[3]=findDifference(H,newH_270)

for a0 in xrange(q):
    angle = int(raw_input().strip())
    # your code goes here
    angle=angle%360
    noOfRotations=angle/90
    print changes[noOfRotations]









