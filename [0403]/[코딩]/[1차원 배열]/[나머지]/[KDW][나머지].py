A=[]
for i in range(10):
# 10번 입력받음
    A.append(int(input())%42)
# 입력값을 42로 나눈 나머지를 A리스트에 추가
print(len(set(A)))
# A리스트에서 set을 통해 중복값을 제거 후 리스트의 크기를 출력
     
    
