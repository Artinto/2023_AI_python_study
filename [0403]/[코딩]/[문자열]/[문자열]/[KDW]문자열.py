case = int(input())
A = []
for i in range(case):
  # CASE번 입력 받음
    A.append(str(input()))
for i in range(case):
    print(A[i][0]+A[i][-1])
    #A리스트 순서대로 1번째 문자와 [-1]을 통해 마지막 문자를 출력
