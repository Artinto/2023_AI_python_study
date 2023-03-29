A, B = input().split()

A = int(A[::-1]) # [::-1] 역순 연산자
B = int(B[::-1])

print(A) if A > B else print(B)
