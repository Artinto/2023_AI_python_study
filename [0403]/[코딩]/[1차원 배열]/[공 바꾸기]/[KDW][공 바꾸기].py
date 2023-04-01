N , M = map(int,input().split())
# N , M입력
if 1<= N <= 100 and 1<=M<=100:
# N , M 조건
    A = []
  # 빈리스트 선언
    for a in range(N):
        A.append(a+1)
        # 리스트에 1~ N 까지 공 번호 입력
    for a in range(M):
        i , j = map(int, input().split())
        if 1 <= i <= j <= N :
          # 공은 1 ~ N까지 있으므로 조건 입력
            temp = A[i-1]
            # i번 공의 리스트를 TEMP 임시 저장
            A[i-1] = A[j -1]
            # I번 바구니에 J번 공을 바꿈
            A[j-1] = temp
            # J번 바구니에 TEMP에 저장한 I번 공을 넣음
        
    for a in range(N):
        print(A[a], end = " ")
    
