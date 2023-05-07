import sys
N, M = map(int,input().split())

test_int_key = {} # 정수형태의 포켓몬리스트 인덱스를 저장할 곳 선언
test_str_key = {} # 문자열형태의 포켓몬리스트 인덱스를 저장할 곳 선언

for i in range(N):
    poketmon = sys.stdin.readline().strip() # 문자열의 양끝 공백을 제거
    test_int_key[i] = poketmon
    test_str_key[poketmon] = i

for _ in range(M):
    item = sys.stdin.readline().strip()
    if item.isdigit() == True : # 입력받은 시험문제에 대해 숫자로 받았는지 확인
        print(test_int_key[int(item)-1])
    else:
        print(test_str_key[item]+1)
