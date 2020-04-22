import re
import fileinput
x=[]
y=[]
z=[]
for line in fileinput.input():
    rex=re.findall(r'\d+',line)
    res = list(map(int, rex)) 
    x.append(res[0])
    y.append(res[1])
    z.append(res[2])
sumx=0
while max(y)>0:
    sumx=sumx+max(y)
    ids=y.index(max(y))
    num=x[ids]
    x.__delitem__(ids)
    y.__delitem__(ids)
    z.__delitem__(ids)
    for q in range (0,len(x)):
        y[q]=y[q]-num*z[q]
print(sumx)
