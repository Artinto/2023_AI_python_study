X=[]; Max=[]
for _ in range(9):
    x=list(map(int, input().split()))
    Max.append(max(x))
    y=Max.index(max(Max))
    X.append(x)
print(max(X[y]))
print(y+1,X[y].index(max(X[y]))+1)
