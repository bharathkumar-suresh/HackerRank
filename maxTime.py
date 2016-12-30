#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     21/12/2016
# Copyright:   (c) sbhar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def findAptValue(gnIntegers,maxVal,ans):
    for each in gnIntegers:
        if each<=maxVal:
            ans=ans+str(each)
            gnIntegers.remove(each)
            break
    return (gnIntegers,ans)


def solution(A,B,C,D):
    gnIntegers=[A,B,C,D]
    gnIntegers=sorted(gnIntegers)
    gnIntegers.reverse()
    print gnIntegers
    ans=''
    (gnIntegers,ans)=findAptValue(gnIntegers,2,ans)
    if ans=='2':
        (gnIntegers,ans)=findAptValue(gnIntegers,3,ans)
    else:
        (gnIntegers,ans)=findAptValue(gnIntegers,9,ans)
    ans=ans+":"
    (gnIntegers,ans)=findAptValue(gnIntegers,5,ans)
    (gnIntegers,ans)=findAptValue(gnIntegers,9,ans)
    if len(ans)<5:
        return "NOT POSSIBLE"
    return ans


def main():
    a=solution(9,1,9,7)
    print a

if __name__ == '__main__':
    main()
