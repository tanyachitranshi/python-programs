x=list(map(int,input().split()))
if len(x)==10:
    x.sort(reverse=True)
    print(x[0])