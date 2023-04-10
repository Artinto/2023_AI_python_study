sample=['c=','c-','dz=','d-','lj','nj','s=','z=']
words=input()
for i in sample:
    words=words.replace(i,' ')
print(len(words))
