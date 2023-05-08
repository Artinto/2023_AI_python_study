import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}
for i in range(1, N+1):
    pockemon = input().strip()
    dict[i] = pockemon
    dict[pockemon] = i
for _ in range(M):
    question = input().strip()
    if question.isdigit():
        print(dict[int(question)])
    else:
        print(dict[question])
