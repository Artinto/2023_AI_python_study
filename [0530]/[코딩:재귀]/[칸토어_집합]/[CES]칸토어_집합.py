import sys

input = sys.stdin.readline


def sol(n, i, j): 
    if n == 0:
        return

    # 3등분
    cnt = (j - i + 1) // 3  # 각각 몇 개씩인지
    # 왼쪽
    sol(n - 1, i, i + cnt - 1)
    # 가운데 -> 공백으로 바꾸기
    for k in range(i + cnt, i + cnt * 2):
        answer[k] = ' '
    # 오른쪽
    sol(n - 1, i + cnt * 2, i + cnt * 3 - 1)


while True:
    try:
        n = int(input())
        answer = ['-'] * (3 ** n)
        sol(n, 0, 3 ** n - 1)
        print(''.join(answer))
    except:
        break
