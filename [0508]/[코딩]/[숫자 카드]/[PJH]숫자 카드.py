N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

answer = {}

for card in cards: # answer에 숫자 카드의 정수를 key로, True를 value로 설정하여 딕셔너리에 추가
    answer[card] = True

for number in numbers:
    if number in answer:
        print(1, end=' ')
    else:
        print(0, end=' ')
