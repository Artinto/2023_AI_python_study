N = int(input())
visited = [False for _ in range(N)]
square = [list(map(int, input().split())) for _ in range(N)]
min_diff = float("inf") # 최소값 구하기 위해 비교할 무한대 

def phy_diff(cnt, n):
    global min_diff
    if cnt == N//2: #탐색한 수가 N의 절반일 때
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    power1 += square[i][j] #스타트 팀 power +1
                elif not visited[i] and not visited[j]:
                    power2 += square[i][j] # 링크 팀 power +1
        min_diff = min(min_diff, abs(power1-power2)) # 무한대와 (스타트팀과 링크 팀의 파워 차이) 중 작은 값 반환
        return

    for i in range(n, N):
        if not visited[i]:
            visited[i] = True
            phy_diff(cnt+1, i+1)
            visited[i] = False

phy_diff(0, 0)
print(min_diff)
