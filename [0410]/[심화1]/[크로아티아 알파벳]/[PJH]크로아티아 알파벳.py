croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i,'*') # 글자 하나씩 i로 for문이 돌면서 i와 비슷한 구간을 하나의 배열 공간으로 바꾸기 위해 place를 사용
print(len(word))
