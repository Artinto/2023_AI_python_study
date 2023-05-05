import sys

n, m = map(int, sys.stdin.readline().split())

names_n = set() # 집합으로 선언
names_m = set()

for _ in range(n):
    name = sys.stdin.readline().strip()
    names_n.add(name)

for _ in range(m):
    name = sys.stdin.readline().strip()
    names_m.add(name)

# 교집합을 이용하여 듣보잡 찾기
common_names = list(names_n & names_m) # 두 이름들의 교집합하여 입력
common_names.sort() # 정렬

print(len(common_names))

for name in common_names:
    print(name)
