C=int(input())
for _ in range(C):
    g=0
    score = list(map(int,input().split()))
    mean=round(sum(score)//score[0])
    for i in range(score[0]):
        if score[i+1]/mean>=1:
            g+=1
    print(f'{g/score[0]*100:.3f}%')
