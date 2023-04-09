word = input().upper()  # 대문자로 변환하여 입력 받음
alpha_count = [0] * 26  # 알파벳의 개수를 저장할 리스트 초기화

# 알파벳 개수 카운트
for i in range(len(word)):
    if word[i].isalpha():  # 알파벳인 경우에만
        alpha_count[ord(word[i]) - ord('A')] += 1  # 현재 문자 word[i]의 알파벳의 인덱스를 alpha_count 리스트 값을 1 증가
        # ord는 문자를 유니코드 넘버로 전환
max_count = max(alpha_count)  # 가장 많이 사용된 알파벳 개수
max_alpha = chr(alpha_count.index(max_count) + ord('A'))  # 가장 많이 사용된 알파벳

if alpha_count.count(max_count) > 1:  # 가장 많이 사용된 알파벳이 여러 개인 경우
    print('?')
else:
    print(max_alpha)
