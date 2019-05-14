num=int(input())
a=0
b=1
if num>0:
    if num==1:
        print(a)
    elif num==2:
        print(a,b,end=" ")
    else:
        print(a,b,end=" ")
        for i in range(2,num):
            c=a+b
            print(c,end=" ")
            a=b
            b=c