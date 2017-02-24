#!/bin/python

import sys

matrixMultiplyMatrix=[[1,2,3],[1,0,0],[0,1,0]]
intitialMatrix=[3,2,1]
hackonacciSequence=[1,2,3]

n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]

def multiplyMatrices(A,B): #Multiply 3by3 matrices
    productMatrix=[[0,0,0],[0,0,0],[0,0,0]]
    #print A,B
    for i in range(0,len(A)):
        Sum=0
        for j in range(0,len(A[i])):
            for k in range(0,len(B)):
                Sum+=A[i][j]*B[j][k]
        productMatrix[i][k]=Sum
    return productMatrix


    #return np.dot(A,B)

def NPowerMatrixMultiply(n):
    if n==1:
        return matrixMultiplyMatrix
    if n%2==0:
        tempMatrix=NPowerMatrixMultiply(n/2)
        return multiplyMatrices(tempMatrix,tempMatrix)
    if n%2==1:
        tempMatrix=NPowerMatrixMultiply(n/2)
        return multiplyMatrices(multiplyMatrices(tempMatrix,tempMatrix),matrixMultiplyMatrix)

def findNthElement(n):
    if n<=3:
        return hackonacciSequence[n-1]
    multipliedMatrix=NPowerMatrixMultiply(n-3)
    #desired3Elts=multiplyMatrices(multipliedMatrix,intitialMatrix)
    return 3*multipliedMatrix[0][0]+2*multipliedMatrix[0][1]+multipliedMatrix[0][2]
    #return desired3Elts[0]

H=[]
for i in range(0,n):
    H.append([])
    for j in range(0,n):
        H[i].append('')
for i in range(0,n):
    for j in range(i,n):
        product=((i+1)*(j+1))**2
        H[i][j]=findNthElement(product)
        #if H[i][j]%2==0:
         #   H[i][j]='X'
        #else:
         #   H[i][j]='Y'
        H[j][i]=H[i][j]
print H



for a0 in xrange(q):
    angle = int(raw_input().strip())
    # your code goes here








