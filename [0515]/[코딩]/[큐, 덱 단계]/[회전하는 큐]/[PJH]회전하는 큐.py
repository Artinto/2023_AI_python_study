from collections import deque # deque 모듈을 사용하기 위해 import한다.

N, M = map(int, input().split()) #큐의 크기 N과 뽑아내려는 수의 개수 M을 입력받는다.

positions = list(map(int, input().split()))#뽑아내려는 수의 위치를 입력받는다.

q = deque(range(1, N+1)) #1부터 N까지의 숫자를 가지는 큐를 생성한다.
cnt = 0 #2번과 3번 연산의 횟수를 카운트하기 위한 변수 cnt를 초기화한다.

for p in positions:
    idx = q.index(p) # 큐에서 뽑아내려는 수의 인덱스를 찾는다.
    # 인덱스가 큐의 길이의 반 이하일 때 (왼쪽으로 회전하는 것이 빠를 때)
    if idx <= len(q) // 2:
        # 회전한 횟수만큼 cnt에 더한다.
        cnt += idx
        # 왼쪽으로 idx번 회전시킨다.
        q.rotate(-idx)
    # 인덱스가 큐의 길이의 반보다 클 때 (오른쪽으로 회전하는 것이 빠를 때)
    else:
        # 회전한 횟수만큼 cnt에 더한다.
        cnt += len(q) - idx
        # 오른쪽으로 (큐의 길이 - idx)번 회전시킨다.
        q.rotate(len(q) - idx)

    # 큐의 맨 왼쪽 원소를 제거한다.
    q.popleft()

print(cnt)
