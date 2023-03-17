A,B,C = map(int,input().split())#map을 이용하여 세 숫자를 정수로 입력받는다.

print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
#각각의 계산을 줄 바꿈을 하여 프린트 한다
