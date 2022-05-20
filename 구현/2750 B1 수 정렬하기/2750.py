N = int(input())

number = list(int(input()) for _ in range(N))

number.sort()
for i in number:
  print(i)