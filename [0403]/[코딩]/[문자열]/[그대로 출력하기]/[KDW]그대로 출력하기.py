A = []
for i in range(100):
# 최대 100번 
    A.append(input())
    # 리스트 추가
    if 0 <len(A[i]) < 100 :
        # A리스트가 비어있거나 최대 100글자 넘어가지 않도록 조건문
        print(A[i])
    else :
        break
