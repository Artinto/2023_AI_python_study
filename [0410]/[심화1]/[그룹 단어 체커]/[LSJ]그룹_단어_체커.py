n=int(input())
cnt=0
for _ in range(n):
    word=input()
    value={word[0]:1}
    for i in range(1,len(word)):
        if word[i]!=word[i-1]:
            if value.get(word[i])!=None:
                break
            else:
                value[word[i]]=1
    else:
        cnt+=1
print(cnt)
