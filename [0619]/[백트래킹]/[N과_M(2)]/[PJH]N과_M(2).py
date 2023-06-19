N, M = map(int, input().split())  # 입력: 공백을 기준으로 정수 N과 M을 입력받고, 각각에 할당
answer = []  # 결과를 저장할 빈 리스트 'answer' 생성하여 M개의 조합을 저장


def backtracking(start):
    if len(answer) == M:  # 'answer' 리스트의 길이가 M과 같으면
        print(" ".join(map(str, answer)))  # 리스트 'answer'의 요소를 문자열로 변환하고 공백으로 구분하여 출력
        return  # 함수 종료

    for i in range(start, N + 1):  # start부터 N까지 숫자를 반복하여 조합 생성
        if i not in answer:  # 숫자 i가 'answer' 리스트에 없으면
            answer.append(i)  # 'answer' 리스트에 숫자 i를 추가
            backtracking(i + 1)  # 재귀적으로 'back' 함수 호출하여 현재 숫자보다 큰 다음 번 숫자인 i+1을 재귀적으로 호출
            answer.pop()  # 탐색이 끝나면 현재 숫자를 제거하여 조합 이전 상태로 돌림


backtracking(1) # 오름차순으로 출력해야하므로 start를 1로 둔다
