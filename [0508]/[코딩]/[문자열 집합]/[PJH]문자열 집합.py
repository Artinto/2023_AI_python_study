n, m = map(int, input().split())  # 집합 S의 개수와 검사해야 하는 문자열 개수를 입력받음

s = set()  # 집합 S를 저장할 set 자료형 생성
for i in range(n):
    s.add(input().rstrip())  # 집합 S를 입력받아 set에 저장

count = 0  # 집합 S에 속하는 문자열의 개수를 카운트할 변수 초기화

for i in range(m):
    if input().rstrip() in s:  # 검사해야 하는 문자열 중 집합 S에 속하는 것이 있다면
        count += 1  # 카운트 증가

print(count)  # 결과 출력
