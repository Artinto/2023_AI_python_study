N = int(input())
li = []
for i in str(N):
    li.append(int(i))
li.sort(reverse=True)
for i in li:
    print(i,end='')
