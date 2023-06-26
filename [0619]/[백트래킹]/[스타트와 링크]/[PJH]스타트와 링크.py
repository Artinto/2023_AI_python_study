import sys

# DFS 함수 정의
def dfs(index, start_team, link_team):
    global answer  # 전역 변수 사용 선언

    if index == N:  # 조합 생성 완료 조건
        if len(start_team) != N // 2 or len(link_team) != N // 2:  # 팀 인원 수 검사
            return

        start_power = 0  # 스타트 팀 능력치 초기화
        link_power = 0  # 링크 팀 능력치 초기화

        # 스타트 팀 능력치 계산
        for i in range(N // 2):
            for j in range(N // 2):
                start_power += S[start_team[i]][start_team[j]]
                link_power += S[link_team[i]][link_team[j]]

        # 능력치 차이 최솟값 갱신
        answer = min(answer, abs(start_power - link_power))

        return

    # DFS로 팀 조합 생성
    dfs(index + 1, start_team + [index], link_team)
    dfs(index + 1, start_team, link_team + [index])

input = sys.stdin.readline  # 표준 입력 사용 준비
N = int(input())  # 사람 수 입력
S = [list(map(int, input().split())) for _ in range(N)]  # 능력치 행렬 입력

answer = float('inf')  # 최솟값 초기화
dfs(0, [], [])  # DFS 알고리즘 시작
print(answer)  # 결과 출력: 능력치 차이의 최솟값
