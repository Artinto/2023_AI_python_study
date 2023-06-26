import sys

def backtracking(x):
    global result
    
    if x == N:  # 모든 행에 퀸을 놓았으면 결과 값 하나 증가
        result += 1
        return
    
    for i in range(N):  # 각 열을 순회하며 퀸 위치 검사
        if not (cols[i] or diag1[x + i] or diag2[x - i + N - 1]):  # 현재 위치의 퀸이 놓여도 문제가 없는지 검사
            cols[i] = diag1[x + i] = diag2[x - i + N - 1] = True
            backtracking(x + 1)  # 문제가 없다면 다음 행으로 이동하여 백트래킹
            cols[i] = diag1[x + i] = diag2[x - i + N - 1] = False

N = int(sys.stdin.readline())  # N 값을 입력 받음

cols = [False] * N  # 각 열에 배치된 퀸의 여부를 저장하는 리스트
diag1 = [False] * (2 * N - 1)  # 대각선1에 배치된 퀸의 여부를 저장하는 리스트
diag2 = [False] * (2 * N - 1)  # 대각선2에 배치된 퀸의 여부를 저장하는 리스트
result = 0  # 배치 가능한 경우의 수를 저장할 변수 초기화

backtracking(0)  # 백트래킹 알고리즘 시작
print(result)  # 결과 값 출력
