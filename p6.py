s1,s2=map(str,input().split())
if(len(s1)!=len(s2)):
    print("no")
x=[s1.count(i) for i in s1]
y=[s2.count(i) for i in s2]

if(x==y):
    print("yes")
else:
    print("no")
