
N=int(input())
# 회원의 수 입력
arr=[]

for i in range (N): 
  a,b = map(str,input().split())
  #회원 수 만큼 나이와 이름을 입력
  arr.append([int(a), i, b]) 
  #리스트에 나이, 순서, 이름을 저장
  #i추가 이유는 입력 받은 순서대로 정렬하기 위해

arr.sort()
#리스트 정렬
for i in range (len(arr)): 
  print("%d %s"%(arr[i][0], arr[i][2]))
  #리스트 길이 만큼 나이와 이름 index를 통해 출력
