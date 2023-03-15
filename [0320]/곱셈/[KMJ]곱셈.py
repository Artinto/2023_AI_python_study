# 초기 코드 (성공)
A = int(input())
num = list(str(input()))
num0 = int(num[0])
num1 = int(num[1])
num2 = int(num[2])
print(A*num2, A*num1, A*num0, A*num0*100 + A*num1*10 + A*num2)


# 최종 코드 (성공)
A = int(input())
num = list(str(input()))
sum = 0
for i in range(3):
    num[i] = int(num[i])
    sum += A*num[i]*10**(2-i)
print(A*num[2], A*num[1], A*num[0], sum)
