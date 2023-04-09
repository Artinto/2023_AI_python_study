test_case = int(input()) # case 넘버 입력

# case for문
for _ in range(test_case):
    a = [] # 빈 리스트 생성
    s = 0 # 총합 변수 초기화
    c = 0 # 평균이상 점수 count 초기화
    a = list(map(int, input().split())) # 점수 개수와 점수들을 입력
    num = int(a[0]) # 점수 개수 저장
    for i in range(num):
        s += float(a[i+1]) # 실수형으로 점수들의 총합을 구함
    avr = round(s/num,3) # 점수들의 평균
    for j in range(num):
        if float(a[j+1]) > int(avr) : # 점수하나하나 평균과 비교
            c += 1 # 평균보다 높을 경우 count 1증가
    result = (c/num)*100 # 평균보다 높은 점수들의 확률 구함
    print(format(result,".3f")+"%") # .3f를 이용하여 소수점 3자리수까지 구함
