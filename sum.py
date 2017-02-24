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

def findIfPair(arr1,arr2,value):
    arr2_Hashed={}
    for each in arr2:
        if not arr2_Hashed.has_key(each):
            arr2_Hashed[each]=1
    for each in arr1:
        compliment=value-each
        if arr2_Hashed.has_key(compliment):
            return True
    return False

def main():
    print findIfPair([1,2,4],[4,3,2],1)

if __name__ == '__main__':
    main()
