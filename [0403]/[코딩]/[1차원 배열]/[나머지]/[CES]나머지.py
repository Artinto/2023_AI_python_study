A = []
# 빈 리스트 생성
for i in range(10):
# 10번 반복
    a = int(input())
# a에 input값 저장
    A.append(a%42)
# a를 42로 나눈 나머지 값 A 리스트에 추가
print(len(set(A)))
# set함수로 중복 된 값을 제거한 A의 길이를 출력
