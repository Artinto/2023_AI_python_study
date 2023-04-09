n, M = map(int, input().split())
N= list(range(1,n+1))
# 1~n+1의 리스트를 생성
for _ in range(M):
    begin,end,mid = map(int, input().split())
    begin -= 1
    end -= 1
    mid -= 1
    # 인덱스 사용시 편하기 위하여 -1해줌
    N[begin:end+1] = N[mid:end+1] + N[begin:mid]
    # begin mid end 와 같은 순서를 mid end begin과 같은 순서로 바꾼다.
    # 인덱스 범위를 지정할 때 두번째 인자의 전까지만 해당되기 때문에 +1을 하여 범위 지정
print(*N)
