N, M = map(int,input().split())
cards = list(map(int, input().split()))

count = len(cards) # for문 횟수 설정

f = [] # 중복 검출 리스트 초기화 및 선언
r = [] # 세 카드의 합을 모아 둘 리스트 초기화 및 선언


if N >= 3 and N <= 100 and M >= 10 and M <=300000:
    # 브루트 포스를 위한 중첩 for문
    for k in range(count):
        for j in range(count):
            for i in range(count):
                f.append(cards[k])
                f.append(cards[j])
                f.append(cards[i])
                f = set(f) # 뽑은 3장의 카드가 중복되서 뽑는 것을 방지 하기 위한 set필터
                s = sum(f) # 중복되지 않은 카드들의 합을 저장
                if len(f) == 3: # set에서 3장의 카드가 뽑혔을 경우만 아래코드를 진행
                    if s <= M:
                        r.append(s)
                f = [] # 중복 검출 리스트 초기화
    print(max(r))
