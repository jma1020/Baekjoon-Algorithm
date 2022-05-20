inp = [int(input()) for _ in range(9)]

y = 1

for i in inp:
  if i == max(inp):
    print(i)
    print(y)
  y += 1
