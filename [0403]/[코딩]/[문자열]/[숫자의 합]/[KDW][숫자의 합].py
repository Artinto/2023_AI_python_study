N = int(input())
a = list(input())
#입력을 리스트로 받아 각 숫자를 각 index에 나눠서 저장
sum = 0
for i in range(N):
    sum += int(a[i])
    # 각 index에 저장된 숫자를 총합하여 sum에 저장
print(sum)
