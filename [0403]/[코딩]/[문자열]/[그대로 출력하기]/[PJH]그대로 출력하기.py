while True :
    try :
        print(input())
    except EOFError :
        break
# 입력이 끝날때 종료를 위해 EOF Error를
#EOEF란 입력값이 없어지는 상황을 받아주는 것이다. error가 났을 때 break를 걸어준다
