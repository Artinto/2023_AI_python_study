croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 크로아티아 알파벳을 리스트에 저장
word = input()
# 문자열을 입력받음
for i in croatia:
    # 크로아티아 알파벳 수 만큼 반복하며 알파벳을 i에 대입
    word = word.replace(i, '*')
    # 입력받은 문자열에 크로아티아 알파벳이 있는 경우 *로 대체
print(len(word))
    # 문자 2,3로 표현해야하는 크로아티아 알파벳을 모두 *로 바꾸어 len을 통해 문자길이 출력
