

n, m = map(int, input().split())
# 도감에 저장할 이름 개수, 출력할 개수

dic_int = {}  
#숫자로 검색 시 사용할 딕셔너리 / key가 숫자
dic_name = {}
#문자열로 검색 시 사용할 딕셔너리 / key가 문자
for i in range(n):
    #도감에 이름을 입력하면 dic_int에는 숫자 순서대로 value 저장
    #dic_name에는 입력한 이름이 key로 value가 숫자로 저장
    name = input().strip()
    #딕셔너리 사용시 rstrip()을 통해 양쪽 공백을 제거하는 것이 안정적
    dic_int[i] = name
    dic_name[name] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        # 입력을 숫자로 입력 받았을 경우 숫자에 대한 인덱스 값 출력
        print(dic_int[int(quest)-1])
    else:
        print(dic_name[quest])
