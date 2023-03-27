d1, d2, d3 = map(int, input().split())
#다이스 입력값 받기
if d1 == d2 == d3:
    print(10000 + d1 *1000)
# 다이스 눈이 모두 같을 경우 결과값
elif d1 == d2:
    print(1000+d1*100)
elif d1 == d3:
    print(1000+d1*100)
elif d2 == d3:
    print(1000+d2*100)
# 2개의 다이스 눈만 같을 경우 결과값
else:
    print(100*max(d1,d2,d3))
# 그 외에 3개 다이스 눈 모두가 다를 경우 결과값 max(a,b,c,...) 함수는 안에 변수 중 가장 큰 값을
반환한다.
