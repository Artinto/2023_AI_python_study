class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if not self.stack:
            return None
        else:
            return self.stack.pop()
    def empty(self):
        if not self.stack:
            return True
        else:
            return False

while True:
    s = input().rstrip()
    if s == '.': # '.'만 있다면 무한루프를 벗어난 후 result로 yes를 반환
        break
    stk = Stack()
    result = 'yes'
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[': # '('와 '['이라면 push함수 실행
            stk.push(s[i])
        elif s[i] == ')': # ')'이라면 아래 조건문 실행
            if stk.empty() or stk.pop() != '(': # 스택이 비어있는 동시에 마지막 입력이 '('이 아니라면
                result = 'no' # result로 'no'반환 for문 break
                break
        elif s[i] == ']': # ']'이라면 아래 조건문 실행
            if stk.empty() or stk.pop() != '[': # 스택이 비어있는 동시에 마지막 입력이 '['이 아니라면
                result = 'no' # result로 'no'반환 for문 break
                break
    if not stk.empty(): # 스택이 비어 있다면 result로 'no' 반환
        result = 'no'
    print(result)
