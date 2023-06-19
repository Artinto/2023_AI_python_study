'''
N과 M(2)에서 수열에 있는 자연수여도 리스트에 추가하는 버전
'''
N, M = map(int, input().split())
seq = []
i = 1
def back(i):
    if len(seq) == M:
        print(*seq, sep = ' ')
        return

    for i in range(i, N+1):
      #if i not in seq: N과 M(2)에서 제거된 코드
        seq.append(i)
        back(i) #(i,i) 순열도 만들어야 하므로 back(i+1)->back(i)
        seq.pop()
back(i)
