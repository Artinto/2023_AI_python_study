N = int(input())
li = []
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    li.append((age, name))
li.sort(key = lambda x : x[0])
for i in li:
    print(i[0],i[1])
