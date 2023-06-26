import sys

input = sys.stdin.readline
N = int(input()) # 숫자의 수
num = list(map(int, input().split())) # 연산자가 적용될 숫자들
sign = list(map(int, input().split())) # 각 연산자의 개수

maximum = -1e9 #-10억
minimum = 1e9 # 10억


def calculate(cnt, total, plus, minus, multiply, divide):
    global maximum, minimum
    if cnt == N:
        maximum = max(total, maximum) # 둘 중 더 큰 값
        minimum = min(total, minimum) # 둘 중 더 작은 값
        return

    if plus:
        calculate(cnt + 1, total + num[cnt], plus - 1, minus, multiply, divide)
    if minus:
        calculate(cnt + 1, total - num[cnt], plus, minus - 1, multiply, divide)
    if multiply:
        calculate(cnt + 1, total * num[cnt], plus, minus, multiply - 1, divide)
    if divide:
        calculate(cnt + 1, int(total / num[cnt]), plus, minus, multiply, divide - 1)
# 각 사칙연산 시의 계
calculate(1, num[0], sign[0], sign[1], sign[2], sign[3])
print(maximum)
print(minimum)
