n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print('Case #%d: %d + %d = %d' %(i+1, a, b, a+b)) # i는 0부터 시작하기 때문에 i에 1을 더해준 값을 사용
