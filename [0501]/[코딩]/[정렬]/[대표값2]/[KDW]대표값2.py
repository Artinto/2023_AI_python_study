x = []
for i in range(5):
    x.append(int(input()))
    #5번의 자연수를 입력 받음
x.sort()
#x리스트 크기대로 정렬하여 아래 index 에 2를 통해 중앙값 출력
print(int(sum(x)/5))
#평균출력
print(x[2])
