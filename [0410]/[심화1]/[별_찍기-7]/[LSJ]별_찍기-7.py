N = int(input())
for i in range(1,2*N):
    if i>N:
        i = 2*N-i
    print(' '*abs(N-i)+'*'+'**'*abs(i-1))

'''
N = int(input())
for i in range(N-1,-N,-1):
    print(" "*abs(i)+'*'*(N-1-abs(i))+'*'+'*'*(N-1-abs(i))+" "*abs(i))
'''
