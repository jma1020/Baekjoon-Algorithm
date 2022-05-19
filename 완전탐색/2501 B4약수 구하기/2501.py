N,K = map(int, input().split())


index = []
for i in range(1, N+1):
  if N % i == 0:
    index.append(i)

if K > len(index):
  print(0)
else:
  print(index[K-1])

