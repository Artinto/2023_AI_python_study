table = [list(map(int, input().split())) for _ in range(9)]
# 한줄씩 9번 반복하며 list에 값 입력
max_num = 0
# max_num을 0으로 초기화
max_row, max_col = 0, 0
# max_row와 max)col을 각각 0으로 초기화
for row in range(9):
# row 변수를 통해 9번 반복 (열 반복)
    for col in range(9):
    # col 변수를 통해 9번 반복 (행 반복)
        if max_num <= table[row][col]:
        # 각각 반복 횟수에 맞는 형과 열의 데이터 값의 최대값을 찾는다
            max_row = row + 1
            # max_row는 찾은 데이터 값에 1을 더한다 왜냐면 주어진 데이터 값에 열의 번호가 적혀있기문때문
            max_col = col + 1
            # max_row의 방식과 동일
            max_num = table[row][col]
            # 반복문을 통해 찾은 최대 값을 max_num에 넣어준다
print(max_num)
# 최대값 출력
print(max_row, max_col)
# 최대값의 행, 열 위치 
