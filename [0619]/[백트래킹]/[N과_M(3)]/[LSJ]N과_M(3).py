'''
N과 M(1) 문제에서 중복이 허용된 유형
if i not in seq을 없애 매 반복문마다 수열에 추가함
'''
N, M = map(int, input().split())
seq = []

def back():
    if len(seq) == M:
        print(*seq, sep = ' ')
        return

    for i in range(1, N+1):
      #if i not in seq: 제거된 코드
        seq.append(i)
        back()
        seq.pop()
back()
