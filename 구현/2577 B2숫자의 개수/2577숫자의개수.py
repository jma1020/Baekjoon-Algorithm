

index = list(int(input()) for _ in range(3))

result = 1
for i in index:
  result *= i

n_list = [int(a) for a in str(result)]

for i in range(10):
  print(n_list.count(str(i)))