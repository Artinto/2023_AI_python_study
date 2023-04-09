N = int(input())
if 1<= N <= 100:
    for i in range(N-1):
        print(' '*(N-i-1) + '*'*(i*2+1)+' '*(N-i-1))
    for j in range(N):
        print(' '*(j) + '*'*(2*(N-j)-1)+' '*(j))
        
#백준에서 출력형식이 잘못 되었다고 나오지만 상세설명 x
#다른 컴파일러에서는 잘 작동
