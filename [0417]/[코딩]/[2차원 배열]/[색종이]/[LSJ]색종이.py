N=int(input())
S=0
all=[[0 for col in range(101)] for row in range(101)]
for _ in range(N):
    x,y= map(int,input().split())
    for row in range(x,x+10):
        for col in range(y,y+10):
            all[row][col]=1
for i in all:
    S+=i.count(1)
print(S)
