N = int(input()) # N=27
arr = [['*' for _ in range(N)] for _ in range(N)] # *로 채워진 27*27 크기의 공간 형성

def draw_star(n, x, y):
    if n == 3: #변의 길이가 3이면
        for i in range(3): 
            for j in range(3):
                if i == 1 and j == 1:
                    arr[x + i][y + j] = ' ' # 중간 빈 칸
                else:
                    arr[x + i][y + j] = '*' # 테두리 *
        return #반환하고 출력

    prev = n // 3 # 9
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: #가운데
                for k in range(prev): #9*9 
                    for l in range(prev): # 사이즈의
                        arr[x + prev + k][y + prev + l] = ' ' # 빈공간
            else:
                draw_star(prev, x + i * prev, y + j * prev) #(9, x+i*9, y+j*9)
# 세 덩어리로 나눠 반복문 진행 => 8개의 점으로 이뤄진 커다란 ㅁ이 있다고 하면 각 점이 이전 단계의 함수값임

draw_star(N, 0, 0)
for i in range(N):
    print(*arr[i],sep = "")
