n, m = map(int, input().split())
a=[q for q in range(1,n+1)]
for _ in range(m):
    i, j ,k = map(int, input().split())
    a = a[:i-1]+a[k-1:j]+a[i-1:k-1]+a[j:]
for w in range(n):
    print(a[w], end=" ")
