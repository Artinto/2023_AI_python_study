def hanoi(n, start, mid, end):
    if n == 1:  # 원판이 1개인 경우
        print(start, end)  # 가장 작은 원판을 시작 장대에서 목표 장대로 이동
        return
    
    hanoi(n-1, start, end, mid)  # 가장 큰 원판을 제외한 나머지 원판들을 시작 장대에서 보조 장대로 이동
    print(start, end)  # 가장 큰 원판을 시작 장대에서 목표 장대로 이동
    hanoi(n-1, mid, start, end)  # 보조 장대에 있는 원판들을 목표 장대로 이동

n = int(input())  # 원판의 개수 입력
move_cnt = 2 ** n - 1  # 이동 횟수 계산
print(move_cnt)  # 이동 횟수 출력
hanoi(n, 1, 2, 3)  # 하노이 탑 알고리즘 호출하여 이동 과정 출력
