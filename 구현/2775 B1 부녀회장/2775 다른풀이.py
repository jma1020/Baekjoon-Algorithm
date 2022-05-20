T = int(input())
for t in range(0, T):
  k = int(input())
  n = int(input())
  floor_0 = [i+1 for i in range(n)]
  for i in range(0, k):
    for i in range(0, n):
        floor_0.append(sum(floor_0[:i+1]))
        print(floor_0)
    for i in range(0, n):
      # print('삭제부분')
      del floor_0[0]


print(floor_0[-1])