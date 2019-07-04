s1,s2=map(str,input().split())
if(len(s1)!=len(s2)):
    print("no")
a=[s1.count(i) for i in s1]
b=[s2.count(i) for i in s2]

if(a==b):
    print("yes")
else:
    print("no")
