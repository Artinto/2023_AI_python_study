def backtracking(idx, n, m, answer):
    if idx == m:  # idx가 m과 같을 때, 즉 M개의 원소를 선택한 경우
        print(' '.join(map(str, answer)))  # answer 리스트의 원소들을 공백으로 구분하여 출력
        return
    for i in range(1, n+1):  # 1부터 N까지의 숫자를 선택
        if not answer or answer[-1] <= i:  # 비 내림차순의 조건을 만족하는지 확인
            answer.append(i)  # 조건을 만족하면 answer 리스트에 i 추가
            backtracking(idx+1, n, m, answer)  # 다음 원소를 선택하기 위해 재귀 호출
            answer.pop()  # 현재 선택한 원소를 제거하고 다음 for 루프로 이동하며 다른 선택을 확인하기 위해 사용

n, m = map(int, input().split())  # N과 M을 입력받음
answer = []  # 찾은 원소들을 저장할 answer 리스트
backtracking(0, n, m, answer)  # 백트래킹 알고리즘을 호출하여 조합 조건에 맞게 수열 찾기 시작
