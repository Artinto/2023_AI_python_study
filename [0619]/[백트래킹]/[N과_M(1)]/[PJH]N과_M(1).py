N, M = map(int,input().split())
answer = []

def back():
    if len(answer) == M: # 리스트의 길이가 M과 같은 경우 아래코드 수행
        print(" ".join(map(str, answer))) # 리스트의 요소들을 문자열로 변환, 공백 구분
        return

    for i in range(1, N+1):
        if i not in answer:
            answer.append(i) # i를 추가
            back() # 재귀적으로 back을 불러옴
            answer.pop() # 마지막으로 추가된 요소 제거

back()
