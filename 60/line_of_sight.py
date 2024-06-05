from random import *
x,y,z,w=[randint(1,18)for _ in"    "]
g=[list("🕳️"*40)for _ in range(20)]
d=abs(z-x)
e=abs(w-y)
s=(x<z)*2-1
t=(y<w)*2-1
D=d-e
while~0:
 g[y][2*x:2*x+2]="👁️"
 if abs(x+y-z-w)<2:break
 if D*2>-e:D-=e;x+=s
 if D*2<d:D+=d;y+=t
for r in g:print(*r,sep="")