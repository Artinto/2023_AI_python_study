N=int(input())
numbers=list(map(int,input().split()))
prime=0
for num in numbers:
    error=0
    for j in range(2,num):
        if num%j==0:
            error+=1
    if error==0:
        prime+=1
if 1 in numbers:
    prime-=1
print(prime)
