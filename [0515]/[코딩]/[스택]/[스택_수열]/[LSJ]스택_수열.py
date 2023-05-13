n = int(input())
stack = []
ans = []
err = 0
cnt = 1
for i in range(n):
    num = int(input())
    while cnt <= num:       
        stack.append(cnt)
        ans.append("+")
        cnt += 1
    if stack[-1] == num:    
        stack.pop()        
        ans.append("-")
    else:                   
        print("NO")         
        err = 1            
        break
if err == 0:
    for i in ans:
        print(i)
