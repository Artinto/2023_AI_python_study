import sys
#sys.stdin.readline()함수를 사용하기 위해 sys모듈을 불러옴
case = int(sys.stdin.readline())
#sys.stdin.readline()이 input()함수보다 빠른 이뉴는 한번에 읽어 버퍼에 저장하는 input()보다
#하나씩 읽어들여 버퍼에 보관하는 stdin.readline()이 더 빠르다. *버퍼 사이즈 차이로 인해 입력이
# 많아질수록 stdin.readline()이 더 빠르게 됨
for case in range(case):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)
    
