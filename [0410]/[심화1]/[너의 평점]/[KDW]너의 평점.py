rate = 0
scoreSum = 0

rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
# 각 grade에 대한 학점을 딕셔너리 사용하여 나중에 grade를 통해 학점총점계산하기 용이
for i in range(20):
    subject, score, grade = input().split()
    # 과목, score, grade를 입력
    if grade == "P":
    # grade가 P인 경우는 if 밑에 코드를 진행하지 않고 다음 순서 loop로 넘어감
        continue
    rate += float(score) * rating[grade]
    # 이수학점 score와 grade에 대응하는 평점을 곱한 값
    scoreSum += float(score)
    # 총 이수학점 계산
print(rate/scoreSum)
    # rate나누기 socreSum을 통해 총 평점 출력
