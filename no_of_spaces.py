st = input()
c = 0
if len(st)<=1000:
    for i in range(len(st)):
        if st[i] == " ":
            c = c + 1
    print(c)