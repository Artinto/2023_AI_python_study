n = int(input())
#정렬할 값 입력
li = []
for i in str(n):
    # n을 문자화하여 숫자하나하나 리스트 인덱스에 따로 저장
    li.append(int(i))

    
li.sort(reverse=True) # 내림차순 정렬
 
for i in li:
    print(i,end='')
    #줄바꿈없이 출력하기 위함
