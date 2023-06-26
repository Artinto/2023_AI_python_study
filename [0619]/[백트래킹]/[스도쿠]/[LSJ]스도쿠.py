import sys
squares = [] # 9*9 스도쿠의 값들을 넣을 리스트
blank = [] # 공백, 0으로 인식되어 있는 값들의 위치 값을 넣을 리스트

for i in range(9):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    squares.append(numbers)

for i in range(9):
    for j in range(9):
        if squares[i][j] == 0:
            blank.append((i, j))

def xline(x, target): # target의 가로 방향 검사
    for i in range(9):
        if target == squares[x][i]: # 같은 줄에 있으면
            return False # 오답
    return True # 아니면 정답

def yline(y, target):
    for i in range(9):
        if target == squares[i][y]:
            return False
    return True

def diagonal(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    # 9*9 스도쿠의 각 3*3 사이즈 칸들 내에서 검
    for i in range(3):
        for j in range(3):
            if a == squares[nx+i][ny+j]:
                return False
    return True


def finish_sudoku(n):
    if n == len(blank): # == blank 다 채웠으면
        for i in range(9):
            print(*squares[i]) # 다 채운 스도쿠 출력
        exit(0)

    for i in range(1, 10):
        x = blank[n][0] # 0,0
        y = blank[n][1] # 0,1 부터 시작

        if xline(x, i) and yline(y, i) and diagonal(x, y, i):
            squares[x][y] = i
            finish_sudoku(n+1) #n +=1 한채로 재귀호출
            squares[x][y] = 0

finish_sudoku(0)
