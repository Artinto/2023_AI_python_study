A, B = map(int, input().split())
L =[]
for i in range(A):
    if A % (i+1) ==0:
        L.append(i+1)
if len(L) < B:
    print(0)
else:
    print(L[B-1])
