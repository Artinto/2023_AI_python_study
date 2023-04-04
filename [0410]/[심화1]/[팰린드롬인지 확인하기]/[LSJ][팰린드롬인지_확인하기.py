word = list(input())
for i in range(1,len(word)//2+2):
    if word[i-1]==word[-i]:
        pass
    if i > (len(word)//2):
        print("1")
        break
    elif word[i-1] != word[-i]:
        print("0")
        break
