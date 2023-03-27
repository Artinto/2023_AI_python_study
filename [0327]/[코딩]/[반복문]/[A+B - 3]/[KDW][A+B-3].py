case = int(input())
#케이스를 입력받아 반복문의 반복 횟수를 지정
for _ in range(case):
#0부터 case까지 1씩 증가시켜 반복문을 수행 이때 _자리에 오는 변수는 0부터 case까지 1씩증가됨(range특성)
    A,B = map(int,input().split())
    print(A+B)
