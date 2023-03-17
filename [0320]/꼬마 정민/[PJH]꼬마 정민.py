from sys import stdin # readline()함수를 사용하기 위해 stdin을 import한다.

A, B, C = map(int, stdin.readline().split()) # map을 이용하여 각각의 A, B, C를 연속해서 받되 공백을 기준으로 구분하여 입력받는다.

print(A + B + C)
