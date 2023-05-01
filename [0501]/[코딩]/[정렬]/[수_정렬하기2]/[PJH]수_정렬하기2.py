n = int(input())  # 수의 개수 입력 받기
nums = []  # 수를 저장할 리스트 초기화

# 수 입력 받기
for i in range(n):
    num = int(input())
    nums.append(num)

# 리스트 오름차순으로 정렬
sorted_nums = sorted(nums)

# 정렬된 수 출력
for num in sorted_nums:
    print(num)

# N = int(input())
# arr = []
#
# for _ in range(N):
#     arr.append(int(input()))
#
# arr2 = arr.sort() # 내림차순으로 정렬, 오름차순일 경우 (reverse=true)
#
# for i in range(N):
#     print(arr[i])
