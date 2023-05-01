list=[]
for i in range(5):
    list.append(int(input()))
list.sort()
# 오름차순 정렬
print(int(sum(list)/len(list)))
print(list[2])
