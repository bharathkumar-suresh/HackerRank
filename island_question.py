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

class Node:
    def __init__(self,val,visited):
        self.value=val
        self.IsVisited=visited

def DFS(x,y,graph):
    graph[x][y].IsVisited=True
    #print x,y,graph[x][y].IsVisited
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            #print i,j
            if graph[i][j].value==1 and graph[i][j].IsVisited==False:
                DFS(i,j,graph)
    return


def findNoOfIslands(matrix):
    count=0
    noOfRows=len(matrix)
    noOfColumns=len(matrix[0])
    islandGraph=[]

    islandGraph.append([])
    for j in range(0,noOfColumns+2):
        node=Node(0,False)
        islandGraph[0].append(node)

    for i in range(0,noOfRows):
        islandGraph.append([])
        node=Node(0,False)
        islandGraph[i+1].append(node)
        for j in range(0,noOfColumns):
            val=matrix[i][j]
            node=Node(val,False)
            islandGraph[i+1].append(node)
        node=Node(0,False)
        islandGraph[i+1].append(node)

    islandGraph.append([])
    for j in range(0,noOfColumns+2):
        node=Node(0,False)
        islandGraph[noOfRows+1].append(node)

    #print len(islandGraph[0])

    for i in range(1,noOfRows+1):
        for j in range(1,noOfColumns+1):
            if islandGraph[i][j].value==1 and islandGraph[i][j].IsVisited==False:
                count+=1
                DFS(i,j,islandGraph)
                #print islandGraph[i][j].IsVisited
    return count


def main():
    #matrix=[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
    matrix=[[1,0,0,0,0],[0,1,0,0,1],[0,0,1,0,0],[0,0,0,0,1]]
    print findNoOfIslands(matrix)

if __name__ == '__main__':
    main()
