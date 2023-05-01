N = int(input())
# 생성자를 구할 분해합을 입력
result = 0
for i in range(1, N+1):
# i를 1씩 증가시키고 각 자리의 숫자를 반복하여 더하고 이를 i와 더해서 생성자를 찾음
    A = list(map(int, str(i)))
    # 각자리의 숫자를 list에 저장하여 밑에 sum을 통해 합을 구함
    result = i + sum(A)
    # 여기서 i는 생성자이고 sum(A)는 각자리의 합
    if result == N:
    # 만약 이 i+sum(A)가 분해합과 같다면 i는 생성자이다.
        print(i)
    
    if i==N:
    # 생성자가 없는 경우이다.
        print(0)
        
#N의 분해합은 N 과 N을 이루는 각 자리의 합 -> 여기서 N을 생성자라고 함
#ex) 245(생성자) -> 256(분해합) = 245(생성자) + 2 + 4 + 5 
