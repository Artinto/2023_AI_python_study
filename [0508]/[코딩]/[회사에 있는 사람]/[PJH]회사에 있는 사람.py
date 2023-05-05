n = int(input())
arr = set()  # 현재 회사에 있는 직원들의 이름을 저장할 집합

for i in range(n):
    name, status = input().split()
    if status == 'enter':
        arr.add(name)  # 출근한 직원의 이름을 집합에 추가
    else:
        arr.remove(name)  # 퇴근한 직원의 이름을 집합에서 제거

# 집합을 리스트로 변환하고, 역순으로 정렬해서 출력
for name in sorted(list(arr), reverse=True):
    print(name)
