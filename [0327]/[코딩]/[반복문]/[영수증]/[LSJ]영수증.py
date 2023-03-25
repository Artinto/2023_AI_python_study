cost = int(input())
number = int(input())
sum_list=[]
for _ in range(number):
    A, B = map(int,input().split())
    sum_list.append(A*B)
if sum(sum_list) == cost:
    print("Yes")
else:
    print("No")
