#import sys
#input = sys.stdin.readline
S = input()
ans = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        ans.add(S[i:j+1])
print(len(ans))
