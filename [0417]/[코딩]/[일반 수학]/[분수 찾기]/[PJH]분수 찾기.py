# 사용자로부터 입력을 받습니다
x = int(input())

# 줄 번호를 1로 초기화합니다
line = 1

# x가 현재 줄 번호보다 크면,
# 줄 번호를 x에서 빼고 1을 증가시킵니다
while x > line:
    x -= line
    line += 1

# 현재 줄 번호가 짝수인 경우,
# 분자와 분모를 계산합니다
if line % 2 == 0:
    numerator = x
    denominator = line - x + 1
# 현재 줄 번호가 홀수인 경우,
# 분자와 분모를 계산합니다
else:
    numerator = line - x + 1
    denominator = x

# 분수를 출력합니다
print(f'{numerator}/{denominator}')
