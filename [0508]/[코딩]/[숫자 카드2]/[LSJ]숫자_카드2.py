import sys
input = sys.stdin.readline
N = int(input())
number = list(map(int, input().split()))
M = int(input())
quest = list(map(int, input().split()))
dic = {}
for i in number:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for j in quest:
    if j in dic:
        print(dic[j], end = " ")
    else:
        print(0, end = " ")
