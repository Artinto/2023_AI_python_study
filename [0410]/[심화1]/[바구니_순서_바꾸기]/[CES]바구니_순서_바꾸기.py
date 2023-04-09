n, M = map(int, input().split())
N= list(range(1,n+1))
for _ in range(M):
    i,j,k = map(int, input().split())
    N=N[:i-1]+N[k-1:j]+N[i-1:k-1]+N[j:]
print(*N)
# print (*N)은 리스트의 모든 요소 값을 공백을 기준으로 출력
