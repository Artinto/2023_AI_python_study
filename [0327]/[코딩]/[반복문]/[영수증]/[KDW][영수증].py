total = int(input())
# 영수증 적힌 총 금액 입력
case = int(input())
# 물건의 종류만큼 반복
sum = 0
# 계산값의 총합을 sum 저장
for x in range(case):
    A,B = map(int, input().split())
    sum += A*B
    # 물건 가격 *개수 금액을 sum에 모두 더하여 총합을 구함
if total == sum:
  #영수증 총 금액과 sum 금액이 같으면 yes
    print("Yes")
else:
    print("No")
