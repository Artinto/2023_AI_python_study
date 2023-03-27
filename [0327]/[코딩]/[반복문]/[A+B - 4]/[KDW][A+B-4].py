while True:
#while 반복문 : 뒤에 조건 작성문 작성부분에 TRUE를 작성하여 무한반복을 수행
    try:
    # 반복 시 수행되는 부분
        A,B = map(int,input().split())
        print(A+B)
    except:
    # 예외 발생 시 실행되는 부분으로 break 작성 시 반복문을 탈출
        break
