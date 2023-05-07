import sys

N = int(input())
cards = [*map(int,sys.stdin.readline().split())] # 리스트에 append를 사용한 구문을 간결히 작성
M = int(input())
numbers = [*map(int,sys.stdin.readline().split())]

arr = {} # 출력에 대한 index선언

for card in cards:
    if card in arr: # arr에 card와 같은 수가 있다면 +1, 아니면 1을 저장
        arr[card] += 1
    else:
        arr[card] = 1
        
for num in numbers:
    if arr.get(num) == None: # arr에 num과 같은 숫자의 인덱스가 없다면 0, 있다면 그 인덱스 안에 있는 수를 출력
        print(0, end=' ')
    else:
        print(arr.get(num), end=' ')
