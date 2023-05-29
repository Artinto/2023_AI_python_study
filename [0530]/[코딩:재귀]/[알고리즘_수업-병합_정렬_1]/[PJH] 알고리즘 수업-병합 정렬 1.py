def merge_sort(A, p, r):  # A[p ~ r]을 오름차순 정렬한다.
    if p < r:
        q = (p + r) // 2  # q는 p, r의 중간 지점
        merge_sort(A, p, q)  # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)  # 병합

def merge(A, p, q, r):
    global cnt, res
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:  # 왼쪽 배열과 오른쪽 배열의 요소를 비교
            tmp.append(A[i])  # 작은 값을 임시 배열에 추가
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])  # 남은 요소를 임시 배열에 추가
        i += 1

    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])  # 남은 요소를 임시 배열에 추가
        j += 1

    i = p
    t = 0

    while i <= r:  # 결과를 A[p~r]에 저장
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:  # K번째로 작은 수를 찾은 경우
            res = A[i]  # 결과 변수에 할당
            break;
        i += 1
        t += 1

N, K = map(int, input().split())  # 입력값을 N과 K로 분리
A = list(map(int, input().split()))  # 배열 A 입력
cnt = 0  # 카운트 변수 초기화
res = -1  # 결과 변수 초기화
merge_sort(A, 0, N - 1)  # 배열 A를 병합 정렬
print(res)  # 결과 출력
