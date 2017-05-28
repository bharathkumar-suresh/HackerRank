import sy
n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
pattern=['Y','X','Y','X','X','Y','Y']
#check
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

H=[]
for i in range(0,n):
    H.append([])
    for j in range(0,n):
        H[i].append('')
for i in range(0,n):
    for j in range(i,n):
        product=((i+1)*(j+1))**2
        product=product%7
        H[i][j]=pattern[product-1]
        H[j][i]=H[i][j]

newH_90=rotateBy90(H)
newH_180=rotateBy90(newH_90)
newH_270=rotateBy90(newH_180)
changes=[0,0,0,0]
changes[1]=findDifference(H,newH_90)
changes[2]=findDifference(H,newH_180)
changes[3]=findDifference(H,newH_270)
