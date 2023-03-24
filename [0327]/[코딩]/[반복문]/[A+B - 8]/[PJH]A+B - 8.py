from sys import stdin # 효율을 높이기 위해 stdin을 import하여 readline()을 사용하여 효율을 높임

t = int(stdin.readline())

for c in range(t):
    a,b = map(int, stdin.readline().split())
    print("Case #"+str(c+1)+":", a ,"+", b ,"=", (a+b))
    # (c+1)을 #과 :같이 붙여서 출력을 하기 위해 문자열로 변환 시킨 후 +연산자를 이용함
