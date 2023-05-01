# 666, 1666, 2666, 3666, 4666, 5666, 6660, 6661 ...
N = int(input())
cnt = 0
num = 1
while True:
# 무한 반복문
    if "666" in str(num):
# num이라는 문자열 안에 666이라는 문자열이 들어있을 때
        cnt = cnt+1
# cnt에 1을 더해줌
    if cnt == N:
# cnt가 N과 같을 때
        print(num)
        break
    num+=1
# 반복문이 돌 때마다 num을 1씩 더해줌
        
