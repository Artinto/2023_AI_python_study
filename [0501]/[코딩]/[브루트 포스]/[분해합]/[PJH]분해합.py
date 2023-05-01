N = int(input())

for i in range(0,N,1):
    s = i + sum(map(int, str(i))) # i자체의 수와 각 자리의 수를 for문을 통해 더함
    if s == N: # 주어진 수와 같을 경우 아래 코드 진행
        print(i)
        break
else:
    print(0)
