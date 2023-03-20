A,B,C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print( ((A%C) * (B%C))%C)
#값을 넣어보면 1번째 연산과 2번째 연산결과가 같은 것을 확인할 수 있다.
