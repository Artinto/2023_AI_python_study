n = int(input())

stack = [] # stack 초기화
answer = [] # 출력 answer 초기화
count = 1 # count 초기화

for _ in range(n):
    num = int(input())
    while count <= num: # count가 입력된 num과 같거나 클때까지 1씩 증가하며 스택에 쌓으면서 answer에 '+'넣음
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == num: # 스택에 마지막 입력된 값이 num과 같다면 pop을 실행하고 answer에 '-'저장
        stack.pop()
        answer.append('-')
    else:
        print('NO') # 나머지는 만들 수 없는 배열이다라고 판정하여 'NO'출력
        exit(0)
for ans in answer:
    print(ans)
