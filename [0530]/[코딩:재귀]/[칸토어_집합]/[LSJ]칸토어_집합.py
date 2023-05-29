def Cantor(n):
    if n == 0:
        return "-" # n이 0이면 - 1개만 출력
    else:
        prev = Cantor(n-1) # 한 단계 전의 Cantor 정의
        return prev + prev.replace("-"," ") + prev #Cantor는 이전단계의 Cantor+그 수만큼의 공백 + 이전단계의 Cantor
while True:
    try:
        N = int(input())
        print(Cantor(N))
    except:
        break # 입력이 없으면 종료
