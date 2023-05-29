import sys

def draw_star(N, x, y):
    # 기저 조건: N이 1인 경우, 현재 위치에 별 찍기
    if N == 1:
        stars[y][x] = '*'
        return

    div = N // 3  # 패턴의 크기를 계산
    for i in range(3):  # 3x3 패턴을 반복하여 그리기
        for j in range(3):
            if i == 1 and j == 1:
                continue  # 가운데 공백은 건너뛰기
            draw_star(div, x + (div * i), y + (div * j))  # 재귀 호출로 패턴 그리기

# 입력을 받을 때 strip()을 사용하여 개행 문자 제거
N = int(sys.stdin.readline().strip())

# 2차원 리스트 초기화: N x N 크기의 공백으로 채워진 리스트 생성
stars = [[' ' for _ in range(N)] for _ in range(N)]

# 패턴 그리기 함수 호출
draw_star(N, 0, 0)

# 결과를 한 줄씩 출력
for row in stars:
    print(''.join(row))
