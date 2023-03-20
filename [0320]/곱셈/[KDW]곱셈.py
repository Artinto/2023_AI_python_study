input1 = int(input())
# 1번째 입력값 
input2 = input()
# 2번째 입력값 문자열의 index를 연산에 이용하기 위해 int를 받지 않음
num1 = int(input2[2]) * input1
num2 = int(input2[1]) * input1
num3 = int(input2[0]) * input1
num4 = input1 * int(input2)
# 1번째 입력값과 2번째 입력값의 각 자리 숫자들과 곱 연산을 통해 결과값의 각 자리를 계산
print(num1,num2,num3,num4, sep='\n')
#결과를 차례로 출력
