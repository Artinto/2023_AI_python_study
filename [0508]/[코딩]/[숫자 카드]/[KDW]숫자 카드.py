n = int(input())
arr = set(map(int,input().split()))
# set으로 저장 할 경우 아래 if in 를 통해 비교할 때 시간 복잡도가 list를 사용할 때 보다 더 효율이 좋음
m = int(input())
m_arr= list(map(int,input().split()))
for i in range(m):
    if m_arr[i] in arr : 
        print(1,end=' ')
        # 처음 입력한 카드와 2번째 입력한 카드를 비교하여 1 출력
        # end = ' ' 한칸 씩 띄어서 출력하기 위함
    else : 
        print(0,end=' ')

