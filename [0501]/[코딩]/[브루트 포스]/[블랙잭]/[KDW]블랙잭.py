N, M = map(int, input().split())
#입력받을 카드의 개수와 3장의 입력카드의 최대값을 입력
arr = list(map(int, input().split()))
#카드를 N개만큼 입력
result = 0
for i in range(N):
    #여기서 3중 중첩 반복문을 사용한 이유는 3장의 카드의 모든 경우의 수를 찾기 위함
    # 1번째 카드의 INDEX가 i
    for j in range(i+1, N):
        # 2번째 카드의 INDEX가 j
        for k in range(j+1, N):
            # 3번째 카드의 INDEX가 k
            if arr[i] + arr[j] + arr[k] > M:
            #리스트에서 각 index의 데이터를 모두 더해서 M값 보다 크면 계속 반복문 진행
                continue
            else:
            #위 조건에 해당하지 않은 경우 조건에 충족하기 때문에 result에 총합의 저장하여 최종적으로 가장 큰 값을 저장
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)
