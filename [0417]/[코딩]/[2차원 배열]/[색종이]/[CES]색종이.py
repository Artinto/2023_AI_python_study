N = int(input())
# 색종이의 개수 N에 대입
array = [[0]* 100 for _ in range(100)]
# [100,100]행렬을 0으로 채움
for _ in range(N):
# N번 반복
    y1, x1 = map(int, input().split())   
# y위치와 x위치 각각 입력받아서 대입
    for i in range(x1, x1 + 10):
# 도화지안에 있는 색종이의 x길이 만큼 반복
        for j in range(y1, y1 + 10):
# 도화지 안에 있는 색종이의 y길이 만큼 반복
            array[i][j] = 1      
# 반복문 돌린 i와 j값의 위치의 배열 값에 1 넣어줌
result = 0
# result값 0으로 초기화
for k in range(100):
# 100번 반복
    result += array[k].count(1)
# 각 행마다 원소가 1로 채워져있는 부분이 있을 때마다 누적하여 1씩 더하고 그 과정을 100번 반복
print(result)
# 앞에서 구한 result의 값을 넓이로써 출력
