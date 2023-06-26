import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3 # 주어진 행 x가 속한 3x3 사각형 영역의 왼쪽 위 행 인덱스
    ny = y // 3 * 3 # 주어진 열 y가 속한 3x3 사각형 영역의 왼쪽 위 행 인덱스
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank): # 모든 빈 칸을 채웠을 경우 동작
        for i in range(9):
            print(*graph[i]) # 각 행을 출력, *연산자를 사용하여 리스트를 풀어서 전달하므로 리스트의 요소들이 공백으로 구분되어 출력
        exit(0) # 프로그램 종료

    for i in range(1, 10): # 1부터 9까지 반복하는 루프 시작 즉, 가능한 모든 숫자 시도
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
          # 모든 함수의 결과값이 True이면 동작
            graph[x][y] = i
          # 현재 위치에 i를 넣음
            dfs(idx+1)
          # 다음 빈 칸으로 이동하여 dfs함수를 재귀적으로 호출
            graph[x][y] = 0
          # 초기화

dfs(0)
