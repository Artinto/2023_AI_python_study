N = input()
# N에 input값 저장
numbers = map(int, input().split())
# 공백을 기준으로 input값 각각 저장
sosu = 0
# sosu 초기값 0으로 저장
for num in numbers:
# 문자 개수만큼 반복
    error = 0
  # error 값 0으로 설정
    if num > 1 :
      # num이 1보다 크면 (1은 소수가 아니기 때문)
        for i in range(2, num):
          # 2부터 num-1까지 반복
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)
