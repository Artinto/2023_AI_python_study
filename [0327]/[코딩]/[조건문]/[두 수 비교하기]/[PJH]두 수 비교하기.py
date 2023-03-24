a, b = map(int, input().split())
 if a > b: # 정수로 입력받은 a와 b를 비교하여 a가 b를 초과할 경우의 조건을 사용
     print(">")
 elif a < b: # 정수로 입력받은 a와 b를 비교하여 b가 a를 초과할 경우의 조건을 사용
     print("<")
 else: # 위의 두가지 조건을 모두 충족하지 않은 두 수가 같을 경우를 else로 조건을 사용
     print("==")
