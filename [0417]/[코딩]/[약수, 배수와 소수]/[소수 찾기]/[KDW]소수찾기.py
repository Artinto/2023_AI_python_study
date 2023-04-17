n = int(input())
# 수의 개수 입력
number = list(map(int, input().split()))
# 수 입력 
sosu = 0
# 소수 개수 변수

for num in number:
  # 리스트 값만큼 반복
  if num == 1:
    # 리스트의 값이 1이면 소수 카운트 x
    continue
  
  for x in range(2, num):
    # 1은 나눌필요 없으니 2부터 시작하여 num전까지 반복
    if(num % x == 0):
      # x로 나누어 나머지가 0 인경우 break 카운트 x
      break
  else:
    sosu+=1
    # 나머지 0이 없는 경우 소수 카운트
    
print(sosu)
