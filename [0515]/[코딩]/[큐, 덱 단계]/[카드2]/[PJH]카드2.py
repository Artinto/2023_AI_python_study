import sys
from collections import deque # 첫번째 데이터를 제거할 수 있는 poplef()함수를 사용하기 위해 collections모듈에 있는 deque 설치

n = int(sys.stdin.readline())
cards = deque(range(1, n+1)) # 1 ~ n+1까지 순서대로 list 생성

while len(cards) > 1:
    cards.popleft()  # 제일 위에 있는 카드 버리기
    cards.append(cards.popleft())  # 제일 위에 있는 카드를 아래로 옮기기

print(cards[0])
