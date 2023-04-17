n = int(input())
# 입력
if n == 1:
    print("")
# 입력값이 1인 경우 출력 x
while n!=1:
  # 1이 아닌 경우 계속 반복
    for i in range(2, n+1):
      # 1로 나누는건 의미 x 
        if n% i ==0:
          # 나머지 0인 경우 소인수 분해 실행
            print(i)
            # 나눈 값 출력
            n = n // i
            # 입력값을 i로 나누고 몫을 n으로 넣어 n이 1이 아닐 때까지 몫을 소인수 분해
            break
