# 1부터 N까지의 수로 크기가 M인 수열들 만들기

N, M = map(int, input().split()) # N : 수열을 만들 자연수들의 최댓값, M : 수열의 크기
seq = [] # 생성된 수열을 출력할 리스트

def backtracking(): #함수 정의
    if len(seq) == M: 
        print(*seq, sep=' ')
        return
    for i in range(1,N+1): # 이번 자리에 들어갈 자연수 구하기 위한 반복
        if i not in seq: # 리스트 seq에 없는 수이면
            seq.append(i) #seq에 추가하고
            backtracking() #재귀 --> seq의 길이가 M이면 출력후 return을 통해 반환, 길이가 M이 아니면 반복문 실행
            seq.pop() # 마지막에 추가된 자연수 제거

backtracking() #함수 실행
'''
예시
N = 3, M = 1
seq =[]
반복문 1~4
1: seq에 없으므로 추가-> 길이가 M이 됐으므로 backtracking은 seq 출력, 그 후 pop을 통해 맨 뒤 숫자인 '1' 제거
-> seq = []
2,3 도 마찬가지의 순서로 진행
'''
