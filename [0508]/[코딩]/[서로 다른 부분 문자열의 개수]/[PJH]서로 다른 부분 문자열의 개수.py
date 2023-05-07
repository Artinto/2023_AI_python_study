s = input()  # 문자열 S를 입력받음

substrings = set()  # 중복을 제거하기 위해 set()을 사용

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substrings.add(s[i:j])

print(len(substrings))  # 중복을 제거한 부분 문자열의 개수 출력
