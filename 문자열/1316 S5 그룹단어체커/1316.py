N = int(input())

list = list(input() for _ in range(N))

count = N

for i in list:
  for j in range(len(i)-1):
    if i[j] != i[j+1]:
      if i[j] in i[j+1:]:
        count -= 1
        break
    
print(count)