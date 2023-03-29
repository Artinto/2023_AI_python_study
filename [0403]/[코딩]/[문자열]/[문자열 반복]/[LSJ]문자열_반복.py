T = int(input())
for i in range(T):
    R, S=list(map(str,input().split()))
    for j in range(len(S)):
        print(int(R)*S[j], end="")
    if i==(T-1):
        break
    print("")
