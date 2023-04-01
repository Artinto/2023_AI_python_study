N = int(input())
a = list(input())  # 입력받은 문자열을 리스트로 변환하여 a에 저장
t = 0
for i in range(N):
    t += int(a[i])
print(t)
