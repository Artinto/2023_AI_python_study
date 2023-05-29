def isPalindrome(s, cnt=0):
    # 문자열의 길이가 1 이하이면 팰린드롬입니다. 반환값으로 1과 호출 횟수를 리턴합니다.
    if len(s) <= 1:
        return 1, cnt

    # 문자열의 첫 번째 문자와 마지막 문자를 비교합니다.
    if s[0] == s[-1]:
        # 첫 번째 문자와 마지막 문자가 같으면, 첫 번째 문자와 마지막 문자를 제외한 부분 문자열에 대해 재귀 호출합니다.
        # 재귀 호출 시 호출 횟수를 1 증가시킵니다.
        return isPalindrome(s[1:-1], cnt + 1)
    else:
        # 첫 번째 문자와 마지막 문자가 다르면, 팰린드롬이 아닙니다. 반환값으로 0과 호출 횟수를 리턴합니다.
        return 0, cnt

# 테스트 케이스 개수 입력
num_tests = int(input())

# 각 테스트 케이스에 대해 팰린드롬 여부와 호출 횟수를 출력합니다.
for _ in range(num_tests):
    # 알파벳 대문자로 구성된 문자열 입력
    s = input().strip()
    # isPalindrome 함수를 호출하여 팰린드롬 여부와 호출 횟수를 반환받습니다.
    palindrome, count = isPalindrome(s)
    # 팰린드롬 여부와 호출 횟수를 출력합니다. 호출 횟수는 1 증가시켜야 합니다.
    print(palindrome, count + 1)
