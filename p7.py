n=list(input())
i=0
while i<len(n):
  temp=n[i]
  n[i]=n[i+1]
  n[i+1]=temp
  i+=2
print("".join(n))  
