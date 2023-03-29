N = int(input())
s = 0

a = list(map(int, input().split()))

m = max(a)

for i in range(N) :
    s += (a[i]/m) * 100

print(float(s)/N)
