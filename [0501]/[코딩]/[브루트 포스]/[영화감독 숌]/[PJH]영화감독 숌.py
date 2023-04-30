N = int(input())

result = [] # '666'을 포함한 수를 넣는 리스트 초기화
i = 0

while True:
    i += 1
    if '666' in str(i): # '666'이 포함된 수를 걸러냄
        result.append(i)
    if len(result) == N : # result 문자열의 길이가 찾고자 하는 N번과 같을 때로 범위를 제한
        print(result[N-1]) # N번째로 작은 수 출력
        break # 무한 for문 탈출

