n = int(input())
cnt = 0
num = 1
while True:
#무한 반복문에서 한번 반복시 num이 증가
    if "666" in str(num):
    # 1씩 증가하는 num값을 문자형식으로 바꿔 666이 있으면 count + 1
        cnt = cnt+1
        
    if cnt==n:
    # count값이 입력받은 n과 같을 경우 해당 num값을 출력
        print(num)
        break
        
    num = num+1
