A = int(input())
B = input() # 문자열의 index를 사용하기 위해 B는 정수 형태로 바꾸지 않는다
A1 = A * int(B[2]) # B의 3번째 위치한 숫자와 A의 곱
A2 = A * int(B[1]) # B의 2번째 위치한 숫자와 A의 곱
A3 = A * int(B[0]) # B의 1번째 위치한 숫자와 A의 곱
AA = A * int(B)
print(A1, A2, A3, AA, sep='\n') # sep='\n'을 이용하여 출력할 때 줄 바꿈
