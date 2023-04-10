num = int(input())

for _ in range(num):
    score = list(map(int, input().split()))
    mean = sum(score[1:])/score[0]
    #score 리스트에 있는 index 중 1부터 끝까지 모두 더한 후 점수의 갯수인 index만큼 나누어 평균을 구함
    cnt = 0
    # 평균을 넘는 점수의 count
    for i in score[1:]:
        # 0인덱스를 제외한 리스트만큼 반복
        if i > mean:
            #i 인덱스의 값이 평균보다 큰 경우 count +1
            cnt += 1
            
    per = (cnt/score[0])*100
    #cnt를 퍼센트로 표현하기 위한 변환
    print('%.3f' %per + '%')
    #소수 3자리까지 출력 후 %
