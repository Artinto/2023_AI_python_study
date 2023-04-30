a, b, c, d, e, f = map(int, input().split())

# 연립 방정식 해 구하기
x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print(x, y)
