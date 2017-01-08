#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     07/01/2017
# Copyright:   (c) sbhar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Node:
    def __init__(self,var):
        self.var=var
        self.left=None
        self.right=None

    def display(self):
        print self.var

def buildTree(ptr,val):
    if val<ptr.var:
        if ptr.left==None:
            ptr.left=Node(val)
            return
        else:
            ptr=ptr.left
            buildTree(ptr,val)
    else:
        if ptr.right==None:
            ptr.right=Node(val)
            return
        else:
            ptr=ptr.right
            buildTree(ptr,val)

def iterFinder(root,val):
    ptr=root
    while(ptr!=None):
        if val<ptr.var:
            ptr=ptr.left
            continue
        elif val>ptr.var:
            ptr=ptr.right
            continue
        else:
            return True
    return False

def recursiveFinder(ptr,val):
    if ptr==None:
        return False
    if ptr.var==val:
        return True
    if val<ptr.var:
        return recursiveFinder(ptr.left,val)
    else:
        return recursiveFinder(ptr.right,val)


def main():
    vals=[5,3,9,1,4,6,8,10,12,14,16,18,-2,-4,-6,-8,0]
    root=Node(vals[0])
    ptr=root
    for i in range(1,len(vals)):
        buildTree(root,vals[i])
    #print iterFinder(root,4)
    print recursiveFinder(root,13)


if __name__ == '__main__':
    main()
