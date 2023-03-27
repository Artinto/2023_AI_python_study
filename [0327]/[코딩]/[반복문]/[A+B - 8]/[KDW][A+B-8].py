case = int(input())
#반복문 횟수 지정
for x in range(case):
# x가 0부터 case값까지 1씩 증가하면 반복문 진행 
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d"%(x+1,A,B,A+B))
# x가 0부터 시작되지만 문제에서 1부터 시작하는 것을 제시하여 +1해줌
