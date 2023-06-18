# 1부터 n까지의 자연수를 중 중복없이 m개의 수를 뽑아 수열들 만들기

N, M = map(int, input().split()) 

seq = [] # 수열을 출력할 리스트 생성
cnt = 1 # 중복된 수열이 생기지 않기 위한 level
def back(cnt):
    if len(seq) == M:
        print(*seq, sep = ' ')
        return

    for i in range(cnt, N+1):
        if i not in seq:
            seq.append(i)
            back(i+1) # n+1번째 자리에 n보다 큰 숫자가 옴으로써 중복된 수열이 없게 됨 -> 1 다음은 2 or 3.  2 다음은 3 or 4....
            seq.pop()
back(cnt)
