a = []
# 빈 리스트 생성
for i in range (9):
    a.append(int(input()))
# 반복문을 통해 리스트 안에 int 값 넣어줌
m = int(max(a))
# 리스트 안의 최대값을 m에 넣어줌
print(m)
for j in range (9):
    if int(a[j]) == m:
        print(j+1)
# 반복문을 통해 최대값의 리스트 위치를 찾아줌
