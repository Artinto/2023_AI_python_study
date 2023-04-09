N = int(input())
# 반복 횟수 입력받음
group_word = 0
for i in range(N):
    word = input()
    error = 0
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
          # 연속된 인덱스 값이 다르면
            new_word = word[j+1:]
            # 다른 값부터 마지막 값 까지 new_word에 저장
            if new_word.count(word[j]) > 0:
              # new_word에서 word[j]와 같은 값이 하나라도 있으면
                error += 1
                # error 발생
    if error == 0:
        group_word += 1
print(group_word)
