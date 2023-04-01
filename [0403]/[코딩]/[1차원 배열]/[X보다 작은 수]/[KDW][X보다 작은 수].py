N, X = map(int, input().split())
count = 0
if N >= 1 and X <= 10000 :
# 문제에서 요구하는 N과 X의 조건 A 리스트 들어가는 정수는 N보다 크고 X보다 작아야함
    A = list(map(int, input().split()))
    for i in range(N):    
        if A[i] < X :
          # 입력값이 X보다 작은 값이 하나라도 있어야함
            count += 1
    if count >= 1 :
      #카운트 값이 1보다 작으면 조건에 해당되지 않기 때문에 출력 X
        for i in range(N) :
            if A[i] < X :
                print(A[i], end = " ")

