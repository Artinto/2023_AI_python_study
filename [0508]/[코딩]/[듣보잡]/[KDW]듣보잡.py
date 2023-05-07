N,M = map(int, input().split())

arr1 = []
#듣도 못한 사람 리스트
arr2 = []
#보도 못한 사람 리스트
for i in range(N):
    a = input()
    arr1.append(a)
    #리스트에 추가
for i in range(M):
    b = input()
    arr2.append(b)

dic = list(set(arr1) & set(arr2))
#리스트를 set(집합)형으로 바꾼 후 & 교집합 연산자를 사용하여 중복되는 것만 저장
dic.sort()
#사전순으로 정렬
print(len(dic))
#듣보잡 수 출력
for i in range(len(dic)):
    print(dic[i])
