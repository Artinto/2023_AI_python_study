a,b,c,d,e,f = map(int, input().split())
# 연립방정식 정의에 필요한 데이터를 입력
for i in range(-999, 1000):
    for j in range(-999, 1000):
        # x와 y가 -999에서 1000까지의 범위이고 그 안에서 모든 경우의 수를 직접 대입하기 위하여 2중 반복문 사용
        if a*i + b*j == c and d*i + e*j == f:
            # x와 y값을 하나씩 대입하여 충족하면 출력
            print(i,j)
