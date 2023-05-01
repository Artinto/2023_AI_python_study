N = int(input())
arr = []

for i in range(N):
    age, name = map(str,input().split())
    arr.append((int(age),i,name)) # 나이가 같을 시 입력 순으로 정렬 해야 하기 때문에 입력했을 시에 i 값을 리스트에 넣어준다

arr.sort() # 나이순으로 오름차순에 나이가 같으면 가입한 순서의 오름차순으로 우선 순위는 리스트에 넣은 순서대로 나이, 입력순, 이름으로 정렬

for member in arr:
    print(member[0], member[2])
