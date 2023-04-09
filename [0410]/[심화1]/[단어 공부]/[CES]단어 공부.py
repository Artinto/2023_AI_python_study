word = input().upper()
# 대문자로 단어 입력받음
word_list = list(set(word))
# 중복 문자 제거한 list만들어 word_list에 저장
cnt = []
# cnt에 빈 리스트 선언
for i in word_list:
    count = word.count(i)
    cnt.append(count)
    
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])
