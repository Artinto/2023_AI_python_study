import sys


N = int(sys.stdin.readline())
temp = {} # 딕셔너리 

for _ in range(N):
    A, B = map(str, sys.stdin.readline().split())
    # 반복문을 통해 이름과 상태를 입력 받음
    if B == "enter":
        #상태가 출근인 경우 temp에 추가
        temp[A] = B
    else:
        #leave일 경우 temp에서 삭제하여 준다.
        del temp[A]

temp = sorted(temp.keys(), reverse=True)
# key값을 기준으로 사전 순의 역순으로 정렬
for i in temp:
    print(i)
