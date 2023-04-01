N = int(input())
#과목 갯수 입력
score = list(map(int,input().split()))
# 진짜 점수 입력
new = 0
# 조작된 점수의 총합 new 변수 선언 초기화
for i in range(N):
    new += score[i] / max(score) * 100
    # 조작된 점수는 진짜 점수를 가장 큰 과목 점수로 나눈 후 100을 곱한 값이며 이를 모두 합한다.
print(float(new/N))
# 총합값에서 과목 수 만큼 나눈 후 출력
