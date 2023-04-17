X = int(input())
# 입력값
line = 1
# 문제에서 제시한 분수가 저장되어있는 형태를 보면 다음과 같다.
# 1줄 = 1/1
# 2줄 = 1/2, 2/1
# 3줄 = 3/1, 2/2, 1/3
# 4줄 = 1/4, 2/3, 3/2, 4/1

while X > line:
  # X값이 큰 경우 
    X = X - line
    # 예) X가 2인경우 X에서 1을 빼면 X= 1, line += 1이로 인해 2가 됨 그리고 while문 탈출 
    line += 1

if line % 2 ==0:
    num1 = X
    num2 = line - X + 1
    
if line % 2 ==1:
    num1 = line - X + 1
    num2 = X
    
print(num1,num2)

#풀지 못하여 풀이를 찾아봐서 문제를 해결.... 이해가 잘 되지 않습니다.
