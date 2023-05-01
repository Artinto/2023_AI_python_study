n,m = map(int,input().split())
# 체스판 크기 저장
board=[]
result=[]
for i in range(n):
    board.append(input())
# 입력된 보드를 저장
for j in range(n-7):
    for k in range(m-7):
# 체스판의 크기가 8x8이기 때문에 각각 -7을 해줌
        draw1 = 0
        draw2 = 0
# 반복문이 새로 시작될 때마다 두 개의 변수를 초기화
        for a in range(j,j+8):
            for b in range(k,k+8):
# 앞에서 지정한 j,k를 기준으로 8x8크기의 체스판 반복
                if (a+b)%2 ==0:
                    if board[a][b] != 'B':
                        draw1 +=1
                    if board[a][b] != 'W':
                        draw2 +=1
                else:
                    if board[a][b] != 'W':
                        draw1 +=1
                    if board[a][b] != 'B':
                        draw2 +=1
# draw1 : 맨 왼쪽 위 칸이 검정일 때 -> case1
# draw2 : 맨 왼쪽 위 칸이 흰색일 때 -> case2
        result.append(draw1)
# case1일 때 다시 칠해야하는 수 저장
        result.append(draw2)
# case2일 때 다시 칠해야하는 수 저장
print(min(result))
# 그 중 가장 작은 result 값 
