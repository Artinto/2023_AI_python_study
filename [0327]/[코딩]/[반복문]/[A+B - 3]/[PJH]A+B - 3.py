t = int(input())  # 테스트 케이스 개수 t를 입력받음

for _ in range(t):  # t 만큼 반복 # 앞에서 받은 카운트 인자를 입력하여 그만큼 반복
    a,b = map(int,input().split()) # 반복할 때마다 더할 정수들을 입력받음
    print(a+b) # 입력받은 정수들을 더해서 출력
