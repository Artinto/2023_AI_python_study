from itertools import combinations 
N, M = map(int, input().split())
cards=list(map(int,input().split()))
ans=0
for cards in combinations(cards, 3):
    S = sum(cards)
    if ans<S<=M:
        ans=S
print(ans)
