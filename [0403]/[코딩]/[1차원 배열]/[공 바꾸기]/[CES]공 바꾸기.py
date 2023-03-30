N, M = map(int, input().split())
a = []
# a에 빈 리스트 선언
for i in range(N):
    a.append(i+1)
# 반복문을 통해 1 ~ 5 까지 빈 리스트 a에 넣어줌
for j in range(M):
    c, d = map(int, input().split())
    temp = a[c-1]
    a[c-1] = a[d-1]
    a[d-1] = temp
# for문 함수를 통해 각 순서에 맞는 바구니를 교환해준다
for i in range(N):
    print(a[i], end=" ")
# 출력되는 enter 제거
