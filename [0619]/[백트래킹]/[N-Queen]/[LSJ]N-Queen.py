N = int(input()) # N*N 판
cnt = 0 # 방법의 횟수
line = [0] * N # x,i를 정하기 위한 열 x번째 열의 i번째 칸

def check(x):
    for i in range(x):
        if line[x] == line[i] or abs(line[x] - line[i]) == abs(x - i): #같은 열이나 대각선 내에 이미 퀸이 있다면
            return False #False
    return True # 아닌 경우들은 True
  
def back(x):
    global cnt
    if x == N:
        cnt += 1
        return # N개의 퀸을 다 놓았다면 cnt +=1 후 반환
    else:
        for i in range(N): # N개의 칸들 중에 퀸을 놓을 수 있는 횟수 확인
            line[x] = i # [x,i]
            if check(x):
                back(x+1)
back(0)
print(cnt)
