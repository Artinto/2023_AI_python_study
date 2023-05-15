from collections import deque
import sys
T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    Queue = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while Queue:
        m_i = max(Queue)
        front = Queue.popleft()
        M -= 1
        if m_i == front:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            Queue.append(front)
            if M < 0:
                M = len(Queue)-1
