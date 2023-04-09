s = str(input())
l = len(s)
r = []
t = 0

# 문자열 뒤집는 for문
for i in range(l):
    r.append(s[((l-1)-i)])

# 문자열 비교 for문
for j in range(l):
    if s[j] != r[j] :
        t += 1

# true false 구분 if문
if t >= 1 :
    print(0)
else :
    print(1)
