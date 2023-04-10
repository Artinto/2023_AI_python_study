N = int(input())
#단어 개수
cnt = N

for i in range(N):
    #N번 반복
    word = input()
    #문자 입력
    for j in range(0, len(word)-1):
        # 문자열 인덱스 만큼 반복
        if word[j] == word[j+1]:
            pass
        #현재 인덱스 문자와 다음 인덱스 문자가 같은 경우 반복문을 계속 실행
        
        elif word[j] in word[j+1:]:
        #현재 인덱스 문자가 이후 인덱스의 문자에 있다면 count-1 후 작은 for문 탈출
            cnt -= 1
            break

print(cnt)
