n = int(input()) # 반복 횟수 입력 받음
for i in range(1, n+1): # 1부터 n까지 반복
    print(' '*(n-i) + '*'*i) # n-i 만큼의 공백과 i만큼의 *을 반복하여 출력
