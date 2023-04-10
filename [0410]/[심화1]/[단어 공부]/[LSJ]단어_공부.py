word=input().upper()
count=[]
for j in list(set(word)):
    count.append(word.count(j))
if count.count(max(count)) > 1:
    print("?")
else:
    print(list(set(word))[count.index(max(count))])
