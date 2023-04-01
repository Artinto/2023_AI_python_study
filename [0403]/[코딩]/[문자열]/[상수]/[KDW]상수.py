A, B = input().split()
A = A[::-1]
# 첫번째는 index의 범위의 시작 두번째는 index의 범위의 종점 마지막 -1은 index 순서를 뒤집는 경우 사용
# ex) 2일경우는 범위에서 2배수의 index만 반환
B = B[::-1]
if A > B:
#뒤집은 후 비교 후 큰 수 출력
    print(A)
else:
    print(B)
