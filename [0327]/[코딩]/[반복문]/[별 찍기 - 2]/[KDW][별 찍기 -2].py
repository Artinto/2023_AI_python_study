case = int(input())
#반복 횟수 지정
for x in range(1, case+1):
# 첫 줄에 1개의 별을 출력해야하기 때문에 1부터 시작하여 반복횟수 + 1 까지 반복하게 지정
    print(" "*(case-x)+ "*"*x)
# 반복 횟수 - x 만큼 공백 후 별을 출력해야하기 때문에 다음과 같이 공백을 출력 별을 출력
