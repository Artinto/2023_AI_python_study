a, b = map(int, input().split())  # 공백을 기준으로 A, B 입력
a, b = divmod(a * 60 + b - 45, 60) # a*60 값과 b-45 값을 더한 후 60으로 나눈 몫과 나머지를 각각 a, b에 대입
print(a % 24, b) # 시간 단위로 바꿔주기 위해 a에 24로 나눈 나머지를 넣어줌


A, B = map(int, input().split())
if A==0:
    C = ((A+12)*60 + B) - 45
    print(C//60+12, C%60)
else:
    C = ((A)*60 + B) - 45
    print(C//60, C%60) # -> 실행 안됨 ??
