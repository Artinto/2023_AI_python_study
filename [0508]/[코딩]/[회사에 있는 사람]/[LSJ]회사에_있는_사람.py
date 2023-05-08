import sys
input = sys.stdin.readline
n = int(input())
stat = dict()
for _ in range(n):
    a,b = map(str,input().split())
    if b == 'enter':
        stat[a] = b
    else:
        del stat[a]
stat = sorted(stat.keys(), reverse=True)
for i in stat:
    print(i)
