n = int(input())
a = [4]
f = 2
b = 1
sum = 0
if n >= 1 and n <= 15 :
    for i in range(1, n+1):
        f += b
        sum = f ** 2
        a.append(sum)
        b = b * 2
    print(a[n])

# 초기 점 4개로 초기화 한 후 규칙이 반복횟수가 증가할 수록 f에 b를 더하여 재설정
# 재설정 된 f를 제곱하여 a배열에 저장
# 반복횟수에 따라 b도 2배씩 증가하여 진행

