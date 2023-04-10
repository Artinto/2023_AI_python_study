word = input().upper()
# 입력받은 문자를 모두 대문자로 저장 -> 문자 count 시 소문자 대문자 구분을 안하기 위함
word_list = list(set(word))
# 입력받은 문자열 중 중복받은 문자를 제거 후 저장

cnt = []
# 빈 리스트 선언
for i in word_list:
  #중복 제거된 word_list만큼 반목문 실행 각 문자들을 i로 놓음
    count = word.count(i)
    # count함수를 통해 word문자열에 있는 i 문자를 count
    cnt.append(count)
    # 빈 리스트 cnt에 count를 저장
if cnt.count(max(cnt)) >= 2:
  #cnt에 저장된 가장 큰 값이 2개 이상인 경우 ?를 출력 -> 가장 많은 문자가 2개 인 것
    print("?")
else:
  # 2개 이상이 아닐경우 가장 많은 문자를 대문자로 출력
    print(word_list[(cnt.index(max(cnt)))].upper())
