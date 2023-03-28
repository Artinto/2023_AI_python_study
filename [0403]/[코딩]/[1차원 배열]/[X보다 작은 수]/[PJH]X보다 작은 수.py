n, x = map(int, input().split())

a = list(map(int, input().split()))
# 배열을 지정하는데 있어 list()를 작성 후, ()안에 유동적인 값을 입력받기 위해 map함수를 작성하여
# 연속으로 n개 만큼 작성

for i in range(n) :
    if a[i] < x :
        print(a[i], end = " ")
# for문을 이용하여 출력할경우 기본값으로 줄바꿈이 들어가 있어 end = ""를 사용하면 줄바꿈을 없애거나
# " "대신 문자를 사용하면 원하는 문자를 입력할 수 있음
