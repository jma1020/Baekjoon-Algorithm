T = int(input())

for _ in range(T):
  n = int(input())
  y = 0
  while n > 0:
    if n % 2 == 1:
      print(y, end=" ")
    n //= 2
    y += 1

    
  
    