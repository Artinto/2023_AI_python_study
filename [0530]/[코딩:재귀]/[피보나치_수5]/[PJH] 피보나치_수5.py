def fibonacci(n):
    if n <= 1:  # n이 1 이하인 경우
        return n  # n을 그대로 반환
    
    return fibonacci(n-1) + fibonacci(n-2)  # n번째 피보나치 수를 계산하기 위해 n-1번째와 n-2번째 피보나치 수를 더함

n = int(input())  # n 입력
print(fibonacci(n))  # n번째 피보나치 수 출력
