N = int(input())
a = map(int, input().split())
b = 0
for num in a:
    error = 0
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
                error += 1  
        if error == 0:
            b += 1  # error가 없으면 소수.
print(b)
