l=list(map(str,input().split()))
print(l)
x=[]
for i in l:
    h,m=map(int,i.split(":"))
    x.append(h*60+m)
x.sort()
print(x)
z=[]
for j in range(len(x)-1):
    z.append(x[j+1]-x[j])
print(z)
z.append(24*60-(x[-1]-x[0]))
print(z)
print(min(z))
