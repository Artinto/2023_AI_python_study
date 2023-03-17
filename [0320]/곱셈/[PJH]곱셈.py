A = int(input()) # A는 입력하는 정수 그대로 사용하기 때문에 int를 붙여 입력받는다.
B = input() # B는 각각의 자리에 수를 뽑아서 사용, 즉 문자열로 하나하나 정장 후 뽑아 사용해야 하기 때문에 그대로 input만 사용해준다.

AxB2 = A * int(B[2]) # 첫째자리 숫자와 곱
AxB1 = A * int(B[1]) # 둘째자리 숫자와 곱
AxB0 = A * int(B[0]) # 셋째자리 숫자와 곱
AxB = A * int(B) # 전체 곱

print(AxB2)
print(AxB1)
print(AxB0)
print(AxB)
