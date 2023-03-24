while True: # True로 반복문을 무한루프로 지정
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
# 무한 루프 안 try와 except를 사용하여 문제가 없다면 try안 코드를 실행하고 예외가 발생하면 except안 코드로 넘어가 break로 반복문을 정지
