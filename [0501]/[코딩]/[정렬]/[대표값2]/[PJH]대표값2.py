arr =[]

for _ in range(5):
    arr.append(int(input()))

avg = sum(arr)//len(arr)
print(avg)

arr2 = arr.sort()

print(arr[2])
