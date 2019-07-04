s=[]
x=int(input())
l=list(map(int,input().split()))[:x] 
for i in range(0,x):
    if (l[i]==i):
        s.append(l[i])
        s.sort()
if(len(s)>0):
    print(*s,sep=" ")
else:
    print(-1)
