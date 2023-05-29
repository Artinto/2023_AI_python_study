def recursion(S, i, j, cnt):
    cnt += 1
    if i >= j: # 1 1 0 1 1
        return 1, cnt
    elif S[i] != S[j]: # i != -i
        return 0, cnt
    else:
        return recursion(S, i + 1, j - 1, cnt) # 0 vs -1 -> 1 vs -2
def isPalindrome(S):
    return recursion(S, 0, len(S) - 1, 0) # 문자열 S. 0, -1까지
T=int(input())
for _ in range(T):
    S = input()
    print(*isPalindrome(S))
'''
def recursion(S, i, j):
    global cnt  # 함수 내에서 전역 변수로 cnt를 활용하기 위해 global로 명시해준다.
    cnt += 1
    if i >= j: # 1 1 0 1 1
        return 1
    elif S[i] != S[j]: # i != -i
        return 0
    else:
        return recursion(S, i + 1, j - 1) # 0 vs -1 -> 1 vs -2
def isPalindrome(S):
    return recursion(S, 0, len(S) - 1) # 문자열 S. 0, -1까지
T=int(input())
for _ in range(T):
    S = input()
    cnt =0
    print(isPalindrome(S), cnt)
'''
