inp1=int(input())
l=list(map(int,input().split()))
b=l[1:inp1:2]
c=l[0:inp1:2]
if sum(b)>=sum(c):
    print(sum(b))
else:
    print(sum(c))
