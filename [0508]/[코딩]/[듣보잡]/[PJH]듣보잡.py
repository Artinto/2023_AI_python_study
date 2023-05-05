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

# N, M = map(int, input().split())
#
# people = [] # 모든 사람들의 이름을 담을 리스트 초기화
#
# for _ in range(N+M): # N+M번 반복하며, 모든 사람의 이름을 입력받아 리스트에 저장
#     people.append(sys.stdin.readline().strip())
#
# # 슬라이싱을 이용하여 들도 못한 사람 , 보도 못한 사람 따로 저장
# non_listen = people[:N]
# non_shown = people[N:N+M]
#
# unknown = [] # 듣도 볻도 못한 사람 리시트 초기화
#
# for target in people: # 사람들의 이름을 가지고 for문을 돌림
#     if target in non_listen and target in non_shown: # 사람 이름들 중 듣도 보도 못한 사람을 unknown에 저장
#         unknown.append(target)
#
# unknown = set(unknown) # 중복제거 필터
#
# print(len(unknown))
#
# for name in sorted(unknown): # set함수와의 충돌오류로 인해 unknown을 정렬한 순으로 출력
#     print(name)
