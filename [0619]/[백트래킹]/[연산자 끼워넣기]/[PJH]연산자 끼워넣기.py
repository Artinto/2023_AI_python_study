import sys

input = sys.stdin.readline  # 표준 입력을 사용하기 위한 준비
N = int(input())  # 숫자의 개수 N 입력 받음
numbers = list(map(int, input().split()))  # N개의 숫자 입력 받음
ops_count = list(map(int, input().split()))  # 4개의 연산자 개수 입력 받음

maximum = -1e9  # 결과의 최댓값을 저장하기 위한 변수 (초기값은 아주 작은 값)
minimum = 1e9  # 결과의 최솟값을 저장하기 위한 변수 (초기값은 아주 큰 값)

# 깊이 우선 탐색(DFS) 알고리즘을 사용한 함수 정의
def dfs(depth, total, add, subtract, multiply, divide):
    global maximum, minimum  # 전역 변수 사용 선언
    
    # 모든 숫자의 계산이 완료된 경우 동작
    if depth == N: 
        maximum = max(total, maximum)  # 최댓값 갱신
        minimum = min(total, minimum)  # 최솟값 갱신
        return

    # 연산자를 사용하여 가능한 모든 방법을 시도
    if add:
        dfs(depth + 1, total + numbers[depth], add - 1, subtract, multiply, divide)
    if subtract:
        dfs(depth + 1, total - numbers[depth], add, subtract - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * numbers[depth], add, subtract, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / numbers[depth]), add, subtract, multiply, divide - 1)

# 연산을 시작할 때, 첫 번째 숫자는 계산에 사용되지 않으므로 1부터 시작
dfs(1, numbers[0], ops_count[0], ops_count[1], ops_count[2], ops_count[3])
print(maximum)  # 최댓값 출력
print(minimum)  # 최솟값 출력
