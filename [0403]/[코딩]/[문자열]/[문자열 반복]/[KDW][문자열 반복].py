case = int(input())
for i in range(case):
    R, S = input().split()
    R = int(R)
    # R값을 INT형 변환
    S = str(S)
    # R값을 string형 변환
    if 1<=R<=8 and 1<= len(S) <= 20:
      # R 과 S 문제 조건에 맞게 입력
        for j in range(len(S)):
          #S 문자 만큼 반복
            print(R*S[j],end="")
            # 문자열의 문자 하나하나를 R번 반복하고 한줄에 출력하기 위해 end="" 사용
        print()
        #케이스별 줄바꿈을 위해 사용
    else:
        break
