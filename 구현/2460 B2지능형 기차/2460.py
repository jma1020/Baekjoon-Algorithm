index =[]
total = 0
for i in range(10):
  X, Y = map(int,input().split())
  total = total - X + Y
  index.append(total)


print(max(index))
