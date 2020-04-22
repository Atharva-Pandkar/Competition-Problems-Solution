import math 

def primeFactors(n): 
    le=[]
    while n % 2 == 0: 
        le.append(2) 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            le.append(i) 
            n = n / i 
    if n > 2: 
        le.append(n)
    return le
num=int(input())
lst=[]
lst=primeFactors(num)
summ=1
for x in lst:
    if x>=5:
        summ=summ*2
    else:
        summ=summ*x
print(summ)           

