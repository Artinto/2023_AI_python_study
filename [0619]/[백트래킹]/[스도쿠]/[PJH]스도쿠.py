import sys

def is_valid(x, y, num):
    # 함께 있는 행, 열, 그리고 3x3 정사각형에 현재 숫자가 있는지 확인.
    if num in rows[x] or num in cols[y] or num in squares[(x // 3) * 3 + y // 3]:
        return False
    return True

def solve_sudoku(idx):
    if idx == 81:  # 모든 스도쿠 위치를 순회한 경우
        return True

    x, y = idx // 9, idx % 9  # idx를 row와 col 좌표로 변환
    if board[x][y] != 0:  # 현재 위치가 빈칸이 아닌 경우
        return solve_sudoku(idx + 1)

    for num in range(1, 10):  # 가능한 숫자인 1부터 9까지 탐색
        if is_valid(x, y, num):  # 숫자가 유효한 위치에 있는지 확인
            board[x][y] = num
            rows[x].add(num)
            cols[y].add(num)
            squares[(x // 3) * 3 + y // 3].add(num)

            if solve_sudoku(idx + 1):  # 다음 위치의 스도쿠를 품
                return True

            # 백트래킹: 이 숫자가 올바르지 않은 경우 다시 빈칸으로 되돌리기
            board[x][y] = 0
            rows[x].remove(num)
            cols[y].remove(num)
            squares[(x // 3) * 3 + y // 3].remove(num)

    return False

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]  # 스도쿠 판 입력

rows = [set() for _ in range(9)]  # 각 행에 사용된 숫자 추적용 세트 초기화
cols = [set() for _ in range(9)]  # 각 열에 사용된 숫자 추적용 세트 초기화
squares = [set() for _ in range(9)]  # 각 3x3 구역에 사용된 숫자 추적용 세트 초기화

for i in range(9):  # 사용된 숫자들의 초기 정보를 세트에 추가
    for j in range(9):
        if board[i][j]:
            num = board[i][j]
            rows[i].add(num)
            cols[j].add(num)
            squares[(i // 3) * 3 + j // 3].add(num)

solve_sudoku(0)  # 스도쿠 퍼즐 해결

for row in board:
    print(*row)  # 완성된 스도쿠 판 출력
