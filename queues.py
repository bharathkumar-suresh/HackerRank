# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack:
    def __init__(self):
        self.length=0
        self.stack=[]
    def push(self,value):
        self.stack[self.length]=value
        self.length+=1
    def pop(self):
        self.stack=self.stack[:len(self.stack)-1]
        self.length-=1
    def displayTop(self):
        print self.stack[self.length-1]

noOfQueries=0
noOfQueries=input()
stdStack=Stack()
for i in range(0,noOfQueries):
    eachQuery=input()
