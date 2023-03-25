while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
# 반복 횟수를 모르기 때문에 무한 반복을 사용할 수 있는 while문을 사용함
# except을 통해 더 이상 입력되는 변수가 없다면 break.
