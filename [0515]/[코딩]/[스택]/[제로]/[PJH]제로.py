class stack:
    def __init__(self): # stack 초기화
        self.stack = []
    def push(self, x): # push함수 선언, append를 이용하여 입력값 저장
        self.stack.append(x)
    def pop(self): # pop함수 선언, 마지막 입력된 수를 빼냄
        self.stack.pop()
    def sum(self): # sum함수 선언, stack에 있는 모든 수를 더함
        s = 0
        for i in range(len(self.stack)):
            s += self.stack[i]
        return s
K = int(input())

stk = stack()

for _ in range(K):
    num = int(input())
    if num == 0: # 0을 입력 받으면 pop함수를 불러옴
        stk.pop()
    else:
        stk.push(num) # 0이 아닌 정수 입력시 stack에 저장

print(stk.sum()) # sum함수를 불러와 출력
