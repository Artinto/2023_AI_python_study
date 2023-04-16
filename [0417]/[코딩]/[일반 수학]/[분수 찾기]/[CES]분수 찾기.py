N = int(input())
# 정수 N을 입력받음
line = 1
# line 초기값을 1로 설정
while N > line:
  # 현재의 line값이 N보다 작을 때까지 반복
    N-=line
    # N에서 현재 line값 뺀 후
    line+=1
    # line값 1씩 누적 더함
if line % 2 == 0:
  # line이 짝수면
    a = N
    b = line - N+1
else:
    a = line - N+1
    b = N
print(a, '/',b,sep='')
