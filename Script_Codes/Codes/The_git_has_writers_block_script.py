import re
num=input()
fin=[]
def poss(pos,lens):
    return(pos-lens)
def sub(num):
    lst=[]
    temp = re.findall(r'\d+', num) 
    n=int(temp[0])
    d=0
    while n!=0:
       d=int(n%10)
       lst.append(d)
       n=int(n/10) 
    lst.reverse()
    return lst
    
def case1(n):
    res=[]
    res=sub(n)
    fav=[]
    for x in range (0,len(res)):
        p=0
        if ((x+1)*2>len(res)):
            p=poss((x+1)*2,len(res))
        else:
            p=(x+1)*2
        if res[p-1]==res[x]:
            fav.append(res[x])
    print(sum(fav))
case1(num)
