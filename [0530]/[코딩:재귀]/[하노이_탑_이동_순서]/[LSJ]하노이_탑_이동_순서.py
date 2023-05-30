def hanoi(n, sp, ap, temp): # sp:starting point, ap : arrival point, temp : temporary point
    if n == 1:
        print(sp, ap) #sp에 원판이 1개면 ap로 옮기고 출력
    else: # sp에 원판이 2개 이상일 때
        hanoi(n - 1, sp, temp, ap) #맨 위의 원판 옮기고 나서 다음 ap와의 관계. 이 함수는 원판이 다 떨어질때까지
        print(sp, ap) # 움직인 과정 출력
        hanoi(n - 1, temp, ap, sp) # 이 함수는 ap 가 아닌 temp에 쌓인 원판을 다시 ap로 옮기기 위한 함수
N = int(input())
print(2**N - 1)
hanoi(N, 1, 3, 2)
