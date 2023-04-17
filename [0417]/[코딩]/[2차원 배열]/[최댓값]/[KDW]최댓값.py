import sys
col = 0
row = 0
max_num = 0
#출력 할 행렬 변수 와 최대값 변수
for i in range(9):
  # 9행 9열
  row_num = list(map(int, input().split()))
  # 입력값 저장
  if max(row_num) > max_num:
    # 입력받은 값이 max_num보다 클 경우 조건문 실행
    max_num = max(row_num)
    # max_num이 입력받은 값이 됨
    row = i
    # 행번호 i를 저장
    col = row_num.index(max_num)
    # 반복문 실행시 row_num값이 항상 초기화 -> 인덱스함수를 통해서 열번호를 입력받는 부분
print(max_num)
print(row+1, col+1)
