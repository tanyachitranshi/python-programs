n1, n2 = map(int, input().split())


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)


if n1 <= 100000 and n1 <= 100000:
    swap(n1, n2)
