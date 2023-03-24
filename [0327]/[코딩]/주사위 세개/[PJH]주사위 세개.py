a, b, c = map(int, input().split())

if a == b == c:
    print(10000+(a*1000))
elif a == b or b == c: # a와 b, b 와 c를 비교하며 공통으로 b가 있기때문에 b를 100과 곱함
    print(1000 + (b*100))
elif a == c: # 위의 조건 외의 a와 c의 경우 a를 곱함
    print(1000 + (a*100))
else: # 마지막 조건인 다 다를 경우 max함수를 이용하여 가장 큰 수를 찾아 곱함
    print(max(a, b, c)*100)
