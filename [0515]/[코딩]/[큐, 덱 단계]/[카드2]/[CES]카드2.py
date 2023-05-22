import sys

N = int(sys.stdin.readline())

arr = [i+1 for i in range(N)]

while len(arr) > 1:
    if len(arr) % 2:
        # arr의 길이가 홀수인지 확인
        t = [arr[-1]]
        # 변수 t에 arr의 마지막 요소를 담은 리스트를 할당
        t.extend(arr[1::2])
        #  arr의 두 번째 요소부터 인덱스가 홀수인 요소들을 t에 추가
        arr = t
        # arr을 t로 갱신
    else:
        arr = arr[1::2]
        # arr을 두 번째 요소부터 인덱스가 홀수인 요소들로 갱신

print(arr[0])
