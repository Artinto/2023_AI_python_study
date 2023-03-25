import sys #sys.stdin.readline()는 데이터를 한 줄 단위로 입력받아 일반 input보다 실행 속도가 빠름
n = int(input()) # 반복 횟수를 n에 입력받음
for i in range(n): # n만큼 반복
    a, b = map(int, sys.stdin.readline().split()) # int로 입력받으면 개행문자 알아서 사라짐
    print(a+b)
