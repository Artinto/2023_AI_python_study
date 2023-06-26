import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 2147000000 # 무한대를 나타내는 값으로 INF변수에 저장
res = INF

def DFS(L,idx): # 팀 A에 속한 선수를 선택하는 조합을 구하는 재귀함수
    global res
    if L == N//2: # 팀 A에 선택된 선수의 수가 N//2와 같은 경우 즉, 조합이 완성된 경우 동
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B +=board[i][j]
        res = min(res, abs(A-B)) # 팀 A와 팀 B의 능력치 차이인 abs(A-B)값을 res와 비교하여 최솟값으로 업데이트
        return
    for i in range(idx,N):
        if not visited[i]: # 선수 i가 선택되지 않은 상태라면 아래의 코드 동작
            visited[i] = True 
            DFS(L+1,i+1) # 재귀적으로 다음 단계의 DFS 함수를 호출
            visited[i] = False # DFS 함수를 마치고 돌아오면 백트래킹을 위해 선택된 선수 i의 방문 여부를 다시 Fasle로 변경
          # 이를 통해 다른 조합에서 해당 선수를 선택할 수 있게 함
            
DFS(0,0)
print(res)
