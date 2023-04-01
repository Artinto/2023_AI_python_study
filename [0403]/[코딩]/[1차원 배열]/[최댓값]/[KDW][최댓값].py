A=[]
for i in range(9):
    A.append(int(input()))
#입력 9번을 받아 A리스트에 추가
print(max(A))
#max함수를 통해 A리스트의 최댓값을 구함
print(A.index(max(A))+1)
#리스트.index()에 max(A)함수를 통해 최댓값을 찾게하여 index값을 구한 후 + 1을 해서 몇번째인지 구함 
