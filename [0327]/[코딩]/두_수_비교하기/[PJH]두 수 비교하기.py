a, b = map(int, input().split())
if a > b: # 정수로 입력받은 a와 b를 비교하여 a가 b를 초과할 경우를 조건으로 사용
    print(">")
elif a < b: # 정수로 입력받은 a와 b를 비교하여 b가 a를 초과할 경우를 조건을 사용
    print("<")
else: # 위의 두 경우를 제외 나머지 a와 b가 같을경우를 else로 취급하여 조건으로 사용
    print("==")
