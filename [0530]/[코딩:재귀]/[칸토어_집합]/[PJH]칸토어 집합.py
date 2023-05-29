def cantor_set(N):
    if N == 0:  # N이 0일 경우, 집합의 요소를 '-'로 표시하고 반환한다.
        return '-'

    prev_set = cantor_set(N-1)  # N-1에 대한 칸토어 집합을 재귀적으로 호출한다.
    curr_set = prev_set + ' ' * len(prev_set) + prev_set  # 현재 칸토어 집합은 이전 집합을 중앙에 공백을 추가하여 이어붙인 것이다.

    return curr_set

while True:
    try:
        N = int(input())  # 사용자로부터 정수 N을 입력받는다.
    except EOFError:  # 입력이 더 이상 주어지지 않을 경우, EOFError가 발생하며 루프를 종료한다.
        break
    except ValueError:  # 입력이 정수가 아닐 경우, ValueError가 발생하며 루프를 종료한다.
        break
    else:
        print(cantor_set(N))  # 칸토어 집합을 계산하여 결과를 출력한다.
