a = []

N, M = map(int, input().split())

# list 입력 for문
for c in range(N):
    a.append(int(c)+1) # c는 for문 변수로 0부터 시작하고 입력은 1부터 받아야 하기 때문에 +1

# 값 치환 for문
for t in range(M) :
    i, j = map(int, input().split()) # 몇번째자리 끼리 바꿀지 입력받음
    s = int(a[i-1]) # 바뀌기 전 기존 자리에 있던 값을 임시 저장
    a[i-1] = a[j-1] # i-1자리에 j-1자리 값을 저장
    a[j-1] = s # j-1자리에 기존의 i-1의 값을 저장

# 바꾼 후 list 출력 for문
for u in range(N) :
    print(a[u],end=" ") # end=" "를 이용하여 for문으로 인한 줄바꾸기를 생략
