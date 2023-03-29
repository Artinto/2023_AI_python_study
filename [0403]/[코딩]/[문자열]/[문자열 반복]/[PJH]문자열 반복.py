T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R) # 정수형으로 변환
    S = str(S) # 문자열로 변환
    for i in range(len(S)): # len함수를 이용하여 S문자열의 길이만큼 반복
        print(R*S[i] ,end='')
    print()
