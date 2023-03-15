A,B,C = map(int, input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C)



# print 결과 (A = 5, B = 8, C = 4)
=> 1
=> 1
=> 0
=> 0

# (A+B)%C, ((A%C) + (B%C))%C 가 서로 같은 결과를 나타내는 것을 확인할 수 있다.
# (A*B)%C, ((A%C) * (B%C))%C 가 서로 같은 결과를 나타내는 것을 확인할 수 있다.
