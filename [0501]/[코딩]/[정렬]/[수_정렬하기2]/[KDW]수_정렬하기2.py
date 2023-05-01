import sys

n = int(input())
# 개수 입력
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
    #n개의 데이터 리스트에 저장
num.sort()
#num 리스트 정렬
for i in num:
    print(i)
    #출력
