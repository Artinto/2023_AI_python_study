N = int(input())
A = sorted(list(map(int, input().split())))
#정렬을 통해 작은 수부터 사용하기 위함
M = int(input())
B = list(map(int, input().split()))

cnt = {}
for i in A :
    if i in cnt:
        cnt[i] += 1
    # A리스트에 저장되어 있는 VALUE를 KEY로 하여 딕셔너리 생성
    # 처음 나온 값인 경우 1로 저장하고 그 후 기존에 있던 값이 나오면 + 1
    else:
        cnt[i] = 1
    # 
        
for i in B :
    if i in cnt:
        print(cnt[i], end = ' ')
    #B에 있는 값을 cnt딕셔너리의 key로 활용하여 순서대로 출력
    else:
        print(0, end=' ')
