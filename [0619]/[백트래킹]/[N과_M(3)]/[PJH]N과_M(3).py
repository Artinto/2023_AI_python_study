N, M = map(int, input().split())  # 입력: 공백을 기준으로 정수 N과 M을 입력받고, 각각에 할당
answer = []  # 결과를 저장할 빈 리스트 'answer'를 생성

def backtracking(start):
    if len(answer) == M:  # 기저 조건: 만약 'answer' 리스트의 길이가 M과 같다면
        print(" ".join(map(str, answer)))  # 리스트 'answer'의 요소를 문자열로 변환하고 공백으로 구분하여 출력
        return  # 함수를 종료

    for i in range(start, N+1):  # start부터 N까지 숫자를 반복
        answer.append(i)  # 'answer' 리스트에 숫자 i를 추가
        backtracking(start)  # 재귀적으로 'backtracking' 함수를 호출 (start를 사용하여 같은 숫자를 가능하게 합니다.)
        answer.pop()  # 'answer' 리스트에서 마지막으로 추가된 요소를 제거

backtracking(1)  # 백트래킹 함수 'backtracking'을 시작 숫자 1로 호출
