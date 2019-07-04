num = int(input())
lis = list(map(int,input("").split()))
lis.sort(reverse=True)
k=0
for j in range(num):
  k=k*10+lis[j]
print(k) 
