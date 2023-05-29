N = int(input())  # 정수 N 입력
num = 1  # 변수 초기화: 곱셈 결과를 저장할 변수
pec = 1  # 변수 초기화: 팩토리얼을 계산할 변수

if N >= 0:  # N이 0 이상인 경우
    if N > 0:  # N이 0보다 큰 경우
        for i in range(1, N):  # 1부터 N-1까지 반복
            pec = pec * (N+1-i)  # pec에 N, N-1, N-2, ... 순서로 곱셈을 수행합니다.
    elif N == 0:  # N이 0인 경우
        pec = 1  # pec는 1이 됩니다.
print(pec)  # pec 출력
