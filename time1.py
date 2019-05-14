t = int(input())
def convert(t):
    hours = int(t / 60)
    mins = int(t % 60)
    print(hours , mins)
convert(t)