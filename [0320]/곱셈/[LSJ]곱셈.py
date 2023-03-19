A=int(input()) #주어진 정수값을 A라 선언
B=list(str(input())) #주어진 정수값을 자리수마다 분리 후 B라는 리스트 생성
for i in reversed(B): # 리스트 B를 역순으로 반복
    print(A*int(i)) # 반복문 값 출력
print(A*(int(B[0])*100+int(B[1])*10+int(B[2]))) # 곱셈값 출력
