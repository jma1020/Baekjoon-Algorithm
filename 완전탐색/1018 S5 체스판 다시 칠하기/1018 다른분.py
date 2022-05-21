N, M = map(int, input().split())

count = []

original = [list(input()[:M]) for _ in range(N)]


for a in range(N-7):
  for b in range(M-7):
    first_White = 0
    first_Black = 0
    for i in range(a,a+8):
      for j in range(b,b+8):
        if (i + j) % 2 == 0:
          if original[i][j] != 'W':
            first_White += 1
          if original[i][j] != 'B':
            first_Black += 1
        else:
          if original[i][j] != 'B':
            first_White += 1
          if original[i][j] != 'W':
            first_Black += 1
    count.append(min(first_White,first_Black))

print(min(count))



