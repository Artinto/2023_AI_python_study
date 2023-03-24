total = int(input())
count = int(input())
sum = 0 # 물건의 값과 갯수를 곱한것들을 다 더할 저장공간 생성 및 초기화

for a in range(count):
    cost, n = map(int,input().split())
    sum = sum +(cost*n) # 중첩해서 덧셈

if total == sum:
    print("Yes")
else:
    print("No")
