def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) # fibonacci를 계속 불러와 해당 타겟 목표까지 반복

n = int(input())
print(fibonacci(n))
