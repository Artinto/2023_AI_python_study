N = int(input())
num = 1
pec = 1

if N >= 0:
  if N > 0:
    for i in range(1, N):
      pec = pec * (N+1-i) # N, N-1, N-2 ... 이러한 순서로 곱할 것이기 때문에 N+1-i로 해준다.
  elif N == 0:
    pec = 1
print(pec)
