num = int(input())
lis = list(map(int,input().split()))[:num]
for i in range(num):
  if lis.count(lis[i])==1:
   print(lis[i])
