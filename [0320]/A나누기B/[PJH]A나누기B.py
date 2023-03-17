# 수를 입력 받고 쓰기 위해 readline함수를 중심으로 코딩 작성
from sys import stdin # readline함수를 사용하기 위해 stdin을 import

num1, num2 = map(int, stdin.readline().split()) # 두 정수를 구분하기 위해 공백을 넣어 준 후 map을 이용하여 정수형태로 전환

print(num1 / num2) # 입력 받은 두 정수를 나눈 후 몫을 출력
