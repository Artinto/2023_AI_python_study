N = str(input())

arr = list(N)

arr2 = arr.sort(reverse=True) # 내림차순이기때문에 reverse=True

print(''.join(arr))
