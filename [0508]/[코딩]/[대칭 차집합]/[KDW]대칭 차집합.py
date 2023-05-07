A, B=map(int, input().split())

Alist = set(map(int, input().split()))
Blist = set(map(int, input().split()))

print(len(Alist ^ Blist))
# 파이썬에서 ^ 연산자를 통해 대칭 차집합 연산이 가능하며 이러한 집합 연산은 set(집합)타입에서만 가능 len()을 통해 개수를 출력
