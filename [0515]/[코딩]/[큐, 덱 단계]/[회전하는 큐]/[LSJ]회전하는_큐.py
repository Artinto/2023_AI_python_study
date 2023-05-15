from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
order = list(map(int, sys.stdin.readline().split()))
queue = deque(i for i in range(1,N+1))
cnt = 0
for i in order:
    while 1:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)
