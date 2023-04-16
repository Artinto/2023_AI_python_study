array = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
max_x , max_y = 0, 0

for row in range(9):
    for col in range(9):
        if max_value <= array[row][col]:
            max_x = row + 1
            max_y = col + 1
            max_value = array[row][col]

print(max_value)
print(max_x, max_y)
