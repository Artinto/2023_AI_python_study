class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if not self.stack:
            self.stack = []
        else:
            self.stack.pop()
    def empty(self):
        if not self.stack:
            return True
        else:
            return False

T = int(input())

stk = Stack()

for _ in range(T):
    s = str(input())
    result = 'YES' # 문자열 판단 result 초기화
    for i in range(len(s)):
        if s[i] == '(':
            stk.push(s[i])
        else:
            if stk.empty():
                result = 'NO'
            else:
                stk.pop()
    if stk.empty() and result != 'NO':
        print(result)
    else:
        print('NO')
    stk.stack = [] # stack 초기화
