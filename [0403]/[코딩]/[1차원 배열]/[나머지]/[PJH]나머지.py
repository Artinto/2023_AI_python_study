arr = []
for i in range(10):
    a = int(input()) # 수를 입력 받음
    arr.append(a % 42) # a를 42로 나눈 후 나머지를 arr 배열에 하나씩 저장
print(len(set(arr))) # set함수를 이용하여 중복된 값을 필터를 한뒤 len함수를 이용하여 저장된 데이터 개수를 출력
