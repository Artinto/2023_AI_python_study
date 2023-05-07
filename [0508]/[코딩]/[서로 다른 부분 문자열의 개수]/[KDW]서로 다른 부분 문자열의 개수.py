S=input()
total=set()
for i in range(len(S)):
    for j in range(i,len(S)):
        total.add(S[i:j+1])#i번째 문자부터 j번째 문자까지 부분 문자열 J+1을 통해 J까지
        # 이중반복문과 위와 같은 인덱싱을 통해 S="abc" 일 때,  i=0, j=2일 때는 S [0:2] = "ab"가 추가 이 연산이 반복되면서 a부터 ababc까지 모두 반복

print(len(total))
