a, b, height = map(int,input().split())

current = 0

day = 0
while True:
  day += 1
  current += a 
  if height <= current:
    print(day)
    break
  current -= b

