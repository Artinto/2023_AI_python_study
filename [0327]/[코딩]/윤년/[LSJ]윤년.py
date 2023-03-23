year=int(input())  
if (year%4==0 and year%100!=0) or (year%400==0): 
    print('1') #윤년이면 1 출력
else:
    print('0') #윤년이 아니면 0 출력
