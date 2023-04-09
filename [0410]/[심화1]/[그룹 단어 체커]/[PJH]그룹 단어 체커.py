n = int(input())
count = 0

for i in range(n):
    word = input()
    prev_char = ''
    char_set = set()

    # 각 문자에 대해서 순회하면서 연속되는지 확인한다.
    for char in word:
        if prev_char != char: # 이전 문자와 다를 때
            if char in char_set: # 이전 문자와 다른데 이미 나온 문자인 경우
                break
            char_set.add(prev_char) # 새로운 문자가 나왔으면 char_set에 추가한다.
        prev_char = char
    else: # for문이 정상적으로 다 순회된 경우
        if prev_char not in char_set: # 마지막 문자도 char_set에 추가한다.
            char_set.add(prev_char)
        count += 1 # 그룹 단어이므로 count를 증가시킨다.

print(count)
