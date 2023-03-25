H,M = map(int,input().split())
if M>44:
    print(H,M-45)
elif M<45 and H>0:
    print(H-1,M+15)
else:
    print(23, M+15)
'''
H,M = map(int,input().split())
if M>=45 and H>0:
    print("%s %s" %(H, M-45))
elif M<45 and H>0:
    print("%s %s" %(H-1, 15+M))
else:
    print("%s %s" %(23, M+15))
'''
