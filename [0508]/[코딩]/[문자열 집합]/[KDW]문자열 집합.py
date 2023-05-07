import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())
#N개 만큼 문자열 입력하여 집합 S 생성
cnt = 0
#count할 변수
for _ in range(M):
#집합 S와 비교할 문자열 입력 후 if로 비교하여 카운트
    t = input()
    if t in S:
        cnt+=1
print(cnt)
