'''
   4,5,1,3,2
   1. 4,5,1과 3,2로 쪼갬
   2. 4,5과 1로 쪼개고 3과 2로 쪼갬
   3. 4와 5로 쪼갬 -> 배열의 크기가 각각 1이 됨
   4.(1) 4와 5 병합 ->4,5 => 4 저장, 5 저장
   4.(2) 4,5 와 1 병합 -> 1,4,5 => 1 저장, 4 저장, 5 저장
   5. 3과 2 병합 -> 2,3 => 2 저장, 3 저장
   6. 1,4,5 와 2,3 병합 -> 1,2,3,4,5 => 1 저장, 2 저장, 3 저장, 4 저장, 5 저장
   => 7번째 저장된 수는 3
'''
import sys
input = sys.stdin.readline
N, K = map(int, input().split()) # 1~N, k번째 저장되는 수
arr = list(map(int, input().split())) # 1~N의 수를 문제에 맞게 배치
ans = [] # 병합하는 동안 저장할 리스트 생성
def merge_sort(A):
    if len(A) == 1: #배열의 길이가 1이면 그대로 반환
        return A
    q = (len(A)+1)//2 # 중간값 저장
    left = merge_sort(A[:q]) # 1,4,5
    right = merge_sort(A[q:]) # 2,3
    i, j = 0, 0
    save = [] # 함수 내에서 병합할 때마다 저장할 공간 생성

    while i < len(left) and j < len(right): #left와 right 병합
        if left[i] > right[j]:
            save.append(right[j])
            ans.append(right[j])
            j += 1
        else:
            save.append(left[i])
            ans.append(left[i])
            i += 1
    while i < len(left):
        save.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right):
        save.append(right[j])
        ans.append(right[j])
        j += 1

    return save #save는 save=[]로 다시 반환
#ans는 계속 저장됐으므로 마지막엔 [4,5,1,4,5,2,3,1,2,3,4,5]로 12개의 요소를 갖게 
merge_sort(arr) # 정의된 함수에 [4,5,1,3,2] 대입
if len(ans) >= K: 
    print(ans[K-1])
else:
    print(-1)
'''
함수를 진행하는 동안 save와 ans 모두 저장을 하니 번거로웠는데 해당 과정을 생략하는 방법이 있을지 알고 싶습니다.
'''
