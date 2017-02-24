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

def calculateArea(x1,y1,x2,y2,x3,y3):
    A=float((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1)
    return abs(A/2.0)

def checkIfPointInside(x1,y1,x2,y2,x3,y3,x,y):
    totalArea=calculateArea(x1,y1,x2,y2,x3,y3)
    A1=calculateArea(x1,y1,x2,y2,x,y)
    A2=calculateArea(x2,y2,x3,y3,x,y)
    A3=calculateArea(x3,y3,x,y,x1,y1)
    if totalArea==A1+A2+A3:
        return True
    else:
        return False

#def givenFunction(x1,y1,x2,y2,x3,y3,px,py,bx,by):


def main():
    print 0==calculateArea(0,0,1,1,2,2)
    print checkIfPointInside(0,0,2,0,0,2,1.0,1.01)


if __name__ == '__main__':
    main()
