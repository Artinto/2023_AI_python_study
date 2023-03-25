total = int(input()) # 총합 저장
t = int(input()) # 반복 횟수 저장
sum = 0 # sum을 0으로 초기화
for i in range(t): # t만큼 반복
    A,B = map(int, input().split()) # A와 B 저장
    sum += A*B # A*B 값을 sum에 누적하여 덧셈
if total == sum: # total과 sum의 값이 같으면
    print("Yes") # Yes 출력
else:  # 아니면
    print("No") # No 출력
