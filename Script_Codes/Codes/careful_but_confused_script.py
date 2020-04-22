import fileinput
import statistics 
from statistics import mode 
  
num=int(input())
lst=[]
for lines in fileinput.input():
    lst.append(int(lines))
lst.sort()
count=0
fp=0
md=0
while count!=num:
        md=mode(lst)
        for x in lst:
            if x==md:
                count+=1
                lst.reverse()
                lst.pop()
            lst.sort()   
        lst[-1]=lst[-1]-1
        lst[lst.index(min(lst))]=lst[lst.index(min(lst))]+1
        fp+=1
        lst.sort()
print(fp)   
