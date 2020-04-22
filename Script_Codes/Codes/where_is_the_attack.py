import re
n=input()
a=input()
d=0
o=0
p=0
e=0
b=re.findall(r'[DOPE]',a)
for x in b :
    if x =='D':
        d+=1
    elif x =='O':
        o+=1
    elif x =='P':
        p+=1        
    elif x =='E':
        e+=1        
print(d,o,p,e)   
