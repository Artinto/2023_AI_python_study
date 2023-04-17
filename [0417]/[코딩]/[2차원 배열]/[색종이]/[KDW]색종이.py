paper = [[0] * 100 for _ in range(100)]
# 데이터가 모두 10을 가지는 2차원 배열을 선언
n = int(input())

for _ in range(n):
  #입력받은 N번 만큼 색종이를 붙임
  a, b = map(int, input().split())
  for i in range(a, a+10):
    # 입력받은 a값을 시작으로 a+10까지 반복하여 10cm의 색종이영역을 1로 넣음(x좌표)
    for j in range(b, b+10):
      # (y좌표)
      paper[i][j] = 1
      #2차원 배열에 색종이영역을 1로 넣음
cnt = 0
for box in paper:
  cnt += box.count(1)
  #1로 넣은 값을 카운트하여 넓이 출력

print(cnt)
