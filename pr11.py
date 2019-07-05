n=int(input())
a=list(map(int,input().split()))[:n]
av=int(n/2)
x=a[:av]
y=a[av::]
if sum(x)//len(x)==sum(y)//len(y):
    print("yes")
else:
    print("no")
