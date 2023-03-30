n, x = map(int, input().split())

a = list(map(int, input().split()))

for i in range(n) :
    if a[i] < x :
      # 배열을 통해 i번째 숫자를 불러준 후 x보다 작으면 출력
        print(a[i], end = " ")
