import sys

count_A, count_B = map(int, input().split())

A = set(map(int,sys.stdin.readline().split()))
B = set(map(int,sys.stdin.readline().split()))

print(len(A-B)+len(B-A))
