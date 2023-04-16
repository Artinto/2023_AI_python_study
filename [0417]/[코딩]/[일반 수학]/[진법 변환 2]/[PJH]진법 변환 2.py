# 10진법 N을 B진법으로 변환하는 함수
def convert(num, base):
    # B진법으로 변환한 숫자를 저장할 리스트
    converted_num = []

    while num > 0:
        # 나머지를 구하고 converted_num 리스트에 추가
        remainder = num % base
        if remainder >= 10:  # 나머지가 10 이상이면 알파벳 대문자로 변환하여 리스트에 추가
            converted_num.append(chr(ord('A') + remainder - 10))
        else:
            converted_num.append(str(remainder))
        # 몫을 다시 num으로 대체
        num //= base

    # 리스트에 저장된 숫자를 역순으로 연결하여 B진법으로 변환한 숫자를 얻음
    return ''.join(converted_num[::-1]) # ''.join() 메소드는 문자열 리스트를 하나의 문자열로 변환해줌


# 입력 받기
n, b = map(int, input().split())

# 함수 호출하여 B진법으로 변환한 숫자 출력
print(convert(n, b))
