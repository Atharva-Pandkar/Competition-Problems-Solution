bases=int(input())
num=int(input())
sun=0
lst=[]
mod=0
div=0
while num!=0:
    mod=num%bases
    lst.append(mod)
    num=num-mod
    num=int(num/bases)
lst.reverse()
for x in lst:
    print(x,end="")
