A, B = map(int, input().split())
a=int(str(A)[::-1])
b=int(str(B)[::-1])
if a>b:
    print(a)
else:
    print(b)
