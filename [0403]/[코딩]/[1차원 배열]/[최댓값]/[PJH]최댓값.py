a = [] # 빈 리스트 생성

for i in range(9):
    a.append(int(input())) # append를 사용하여 요소를 추가함

m = int(max(a)) # max함수를 이용하여 리스트 안 최대값을 찾아 저장
print(m)

for j in range(9):
    if int(a[j]) == m: # 리스트 각 자리마다 최대값과 비교
        print(int(j+1)) # 리스트의 자리수는 0부터 시작됨으로 +1을 해줌

