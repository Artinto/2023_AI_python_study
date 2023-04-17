N, K = map(int,input().split())
# N = 약수를 구할 입력값 , K 약수의 순번
result = 0
#
for i in range(1, N+1):
    # 1도 약수이기때문에 포함
    if N%i ==0:
        # 약수일 때 조건문 실행
        K-=1
        # 반복문 실행될 때마다 K를 -1하여 카운트
        if K == 0:
            # K가 0이되면 i가 K번째로 작은 약수 
            
            result=i
            break
        
print(result)
#출력
