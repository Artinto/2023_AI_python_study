A = int(input()) # A에 input 저장
if (A%4==0 and A%100!=0) or (A%400==0): # 윤년 조건
    print('1') # 1출력
else:
    print('0') # 윤년이 아닌 평년일 때 0 출력
