C = list(input())
if 1 <= len(C) <= 100:
#조건
    palindrome = C[::-1]
  #리스트 순서를 뒤집어서 저장
    if palindrome==C:
      #뒤집은 것과 같다면 참 아니면 거짓
        print(1)
    else:
        print(0)
