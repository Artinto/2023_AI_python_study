import sys
input = sys.stdin.readline
n = int(input())
#입력받을 개수 입력
array = []
for i in range(n):
    # n번 동안 x좌표와 y좌표 입력
    x, y = map(int, input().split())
    array.append([y, x])
    #array에 2차원 배열로 데이터 추가
    
sort_array = sorted(array)
#array 정렬
for y, x in sort_array:
    print(x, y)
