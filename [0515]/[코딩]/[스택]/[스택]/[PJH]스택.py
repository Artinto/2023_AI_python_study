import sys
class Stack:
    def __init__(self):# 초기화
        self.stack = []

    def push(self, x):# push함수 선언, stack에 x값 추가
        self.stack.append(x)

    def pop(self):# pop함수 선언, stack이 비어있다면 -1반환, 아니면 pop실행
        if not self.stack:
            return -1
        return self.stack.pop()

    def size(self):# size함수 선언, stack리스트의 길이 반환
        return len(self.stack)

    def empty(self):# empty함수 선언, 비어있다면 1 반환, 아니면 0 반환
        if not self.stack:
            return 1
        return 0

    def top(self):# top함수 선언, 비어있다면 -1 반환, 아니면 마지막 숫자 반환
        if not self.stack:
            return -1
        return self.stack[-1]


stack = Stack()

n = int(input())

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())
