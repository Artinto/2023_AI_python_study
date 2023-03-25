A, B = map(int, input().split()) # 공백을 기준으로 A와 B에 input 입력
if A > B: # A > B 일 때
    print('>') # > 출력
elif A < B: # A < B 일 때
    print('<') # < 출력
else: # 이도저도 아닐 때 (같을 때)
    print('==') # == 출력
    
