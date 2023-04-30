N = int(input()) # 점의 개수 입력
array = [] # 점들의 좌표를 저장할 리스트

for _ in range(N):
    x, y = map(int, input().split()) # 점의 좌표 입력
    array.append((x, y)) # 입력받은 좌표를 리스트에 추가

# 람다식을 이용해 정렬, y좌표 오름차순, y좌표가 같으면 x좌표 오름차순으로 정렬
array = sorted(array, key=lambda x: (x[1], x[0]))
# lambda를 사용하여 따로 함수를 선언하지 않고 익명함수를 사용
# 이 lambda를 사용하여 sorted함수를 이용할 때 정렬기준을 설정하는 key를 첫번째 요소로 할지 두번째 요소로 할지 쉽게 설정 가능

# 정렬된 array의 요소 i를 하나씩 가져와 그 안의 첫번째 요소[0]과 두번째 요소[1]을 출력
for i in array:
    print(i[0], i[1])
