import re
num=int(input())
d=input() 
temp = re.findall(r'\d+', d) 
res = list(map(int, temp)) 
es =  list(map(int, temp)) 
num=len(res)
i=0
chk=3
sul=0
mul=1
for x in range(0,num):
    if res[x]==6 :
        sul=es[x+1]+es[x+2]     
        if res[x+3]<num :
            es[res[chk]]=sul
            chk+=4
    if res[x]==9: 
        mul=es[x+1]*es[x+2]
        if res[x+3]<num :
                es[res[chk]]=mul
                chk+=4
    mul=1
    sul=0
    if res[x]==69:
        break
for x in es:
    print(x,end=" ")
