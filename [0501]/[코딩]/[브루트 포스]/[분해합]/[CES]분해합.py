n = int(input())
for i in range(1, n+1): # 0부터 n번 숫자까지 반복문을 돌린다
    num = sum((map(int,str(i)))) # 자리수의 합
    total = i + num # 분해합을 구한다
    if total ==n: # 분해합과 n이 같으면
        print(i)
        break # 가장 작은 분해합을 구해야하기 때문에 찾는 즉시 break
    if i ==n:
        print(0)
