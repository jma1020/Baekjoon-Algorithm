N = int(input())

inp = list(int(input()) for _ in range(N))

inp.sort()  
for i in inp:
  print(i)