#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     09/02/2017
# Copyright:   (c) sbhar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def findMinimumValue(k,str1):
    if k==0:
        return str1
    if k>=len(str1):
        return "0"

    while(k>0):
        flag=0
        for i in range(0,len(str1)-1):
            #print "Length",i,len(str1)
            if int(str1[i])>int(str1[i+1]):
                flag=1
                str1=str1[:i]+str1[i+1:]
                break
        if flag==0:
            str1=str1[:len(str1)-1]
        k-=1
    return str1

def main():
    print findMinimumValue(2,"9999")
if __name__ == '__main__':
    main()
