import re
p=input()
n=int(p)
digi=input()
rev=re.findall(r'\d+',digi)
re_meta = list(map(int, rev))  
fp=0
final=0
sp=0
for x in re_meta:
    while sp+int(x)<=int(n):
        sp=sp+int(x)
    if sp==int(n):
        fp=1
    if fp==1:
        final=1
    sp=0
sp=0
minv=0
maxv=0
for x in re_meta:
    minv=int(min(re_meta))
    if sp+minv<=n:
        sp=sp+minv
        re_meta[re_meta.index(min(re_meta))]=99999        
    minv=0  
if sp==int(n):
        fp=1
if fp==1:
        final=1
          
            
for x in re_meta:
    if sp+int(max(re_meta))<=int(n):
        sp=sp+int(max(re_meta))
        re_meta[index(max(re_meta))]=0        
if sp==int(n):
        fp=1
if fp==1:
        final=1            
if final ==1:
    print("Possible to achieve exact amount")
else :
       print("Overpaid! These scammers owe me")
