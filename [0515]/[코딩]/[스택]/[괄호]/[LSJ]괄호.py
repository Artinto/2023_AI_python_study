T = int(input())
for _ in range(T):
    stack = []
    target = input()
    for i in target:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print("NO")
