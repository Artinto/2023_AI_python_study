dic={'A+':'4.5','A0':'4.0','B+':'3.5','B0':'3.0','C+':'2.5','C0':'2.0','D+':'1.5','D0':'1.0','F':'0.0','P':'0.0'}
sum=0
total=0
for _ in range(20):
    lecture, p, score = input().split()
    point=float(p)
    total+=point*float(dic[score])
    sum+=point
    if score == 'P':
        sum-=point
        total=total
print(round(total/sum,6))
