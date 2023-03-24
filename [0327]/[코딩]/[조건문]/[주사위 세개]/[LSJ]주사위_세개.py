a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))
'''
lists = list(map(int, input().split()))
for i in range(1,7):
    A = lists.count(i)
    if A == 3:
        print(i*1000+10000)
    elif A == 2:
        print(i*100+1000)
        break
    elif A == 1:
        lists.sort(reverse=True)
        print(lists[0]*100)
        break
    else:
        pass
'''
