system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 진법 바꿀 문자열 system에 대입
N, B = map(int, input().split())
# 각각 input값을 N과 B에 대입
answer = ''
# 빈 문자열 정의
while N != 0:
  # N이 0이 아닐 때 반복
    answer += str(system[N % B])
    # N을 B로 나눈 나머지 값의 system index값을 answer에 하나씩 추가
    N //= B
    # N을 B로 누적하여 나눔
print(answer[::-1])
# 총 들어있는 answer의 문자열을 슬라이스를 통해 뒤집어서 출력
