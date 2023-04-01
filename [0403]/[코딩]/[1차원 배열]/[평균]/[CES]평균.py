A = int(input())
a = list(map(int, input().split()))
m = int(max(a))
s = 0
for i in range(A):
        s += a[i] / m * 100
print(float(s/A))
