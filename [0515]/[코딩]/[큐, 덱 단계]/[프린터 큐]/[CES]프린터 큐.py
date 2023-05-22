from collections import deque
# deque 모듈을 임포트
import sys
# sys 모듈을 임포트
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        # queue가 비어있지 않은 동안 while 루프를 실행
        best = max(queue)  
        # 큐에서 가장 큰 값을 찾아 변수 best에 저장
        front = queue.popleft() 
        # 큐의 왼쪽에서 첫 번째 값을 가져와 변수 front에 저장합니다. 이 값을 큐에서 제거
        m -= 1 
        # 찾으려는 값의 인덱스 m을 1 감소
        if best == front: 
            # 큐에서 가져온 값 front와 가장 큰 값 best가 같은지 비교
            count += 1  
            # 만약 찾으려는 값이 큐의 가장 앞에 있다면, count를 1 증가
            if m < 0: 
                # 만약 찾으려는 값의 인덱스 m이 0보다 작아졌다면, 즉, 찾으려는 값이 큐의 가장 앞에 위치한 경우이기 때문에 아래의 동작 수행
                print(count)
                break

        else:   
            queue.append(front) 
            #  큐의 왼쪽에서 가져온 값을 다시 큐에 추가합니다. 이는 찾으려는 값이 큐의 가장 앞에 있지 않을 때 해당 값을 다시 큐에 넣어서 찾으려는 값이 앞으로 오도록 하는 작업
            if m < 0 : 
                # 만약 찾으려는 값의 인덱스 m이 0보다 작아졌다면, 즉, 찾으려는 값이 큐의 가장 앞에 위치하지 않는 경우
                m = len(queue) - 1 
