#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      sbhar
#
# Created:     21/12/2016
# Copyright:   (c) sbhar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def solution(A):
    # write your code in Python 2.7
    n=len(A)
    startPtr=-1
    endPtr=n
    i=0
    sortedA=sorted(A)
    while(i<n):
        if (A[i]!=sortedA[i]):
            startPtr=i
            break
        i+=1
    if startPtr==-1:
        return 0
    i=n-1
    while(i>=0):
        if (A[i]!=sortedA[i]):
            endPtr=i
            break
        i-=1
    print endPtr,startPtr,endPtr-startPtr+1
    return (endPtr-startPtr+1)



def main():
    A=[1,2,6,5,5,8,9]
    print sorted(A)
    print solution(A)

if __name__ == '__main__':
    main()
