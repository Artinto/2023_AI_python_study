from collections import deque
# deque는 양쪽 끝에서의 append와 pop 연산을 빠르게 수행할 수 있는 자료구조
import sys
#  sys 모듈을 임포트
input = sys.stdin.readline
# input 함수를 sys.stdin.readline으로 재정의
n, m = map(int, input().split())    
# 공백으로 분리된 입력 값을 받아 정수로 변환하여 변수 n과 m에 저장
position = list(map(int, input().split()))  
# 공백으로 분리된 입력 값을 받아 정수로 변환하고 리스트로 저장
dq = deque([i for i in range(1, n+1)]) 
#  1부터 n까지의 숫자로 이루어진 리스트를 생성하여 deque로 변환
count = 0   
#  요소의 이동 횟수를 저장하기 위한 변수 count를 초기화
for i in position:  
    while True:     
        if dq[0] == i:  
            # 큐의 가장 앞에 있는 요소와 찾고자 하는 요소 i가 같은지 비교
            dq.popleft()
            # 큐의 가장 앞에 있는 요소를 제거합니다. 해당 요소를 찾았으므로 큐에서 제거
            break
        else:
            if dq.index(i) < len(dq)/2: 
                #  찾고자 하는 요소 i의 인덱스가 큐의 길이의 절반보다 작은지 비교
                while dq[0] != i:  
                    # 큐의 가장 앞에 있는 요소가 찾고자 하는 요소 i와 다른 동안 반복
                    dq.append(dq.popleft())  
                    # 큐의 가장 앞에 있는 요소를 제거하고, 그 요소를 큐의 맨 뒤에 추가합니다. 이는 큐를 한 칸 회전
                    count += 1
            else:  
                # 큐의 가장 앞에 있는 요소가 찾고자 하는 요소와 다른 경우
                while dq[0] != i:
                    #큐의 가장 앞에 있는 요소가 찾고자 하는 요소 i와 다른 동안 반복
                    dq.appendleft(dq.pop())  
                    count += 1
print(count)
