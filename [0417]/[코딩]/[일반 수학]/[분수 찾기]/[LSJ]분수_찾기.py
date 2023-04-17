X=int(input()); line=1
while X>line:
    X-=line
    line+=1
if line%2==0:
    print(X,'/',line+1-X,sep='')
else:
    print(line+1-X,'/',X,sep='')
