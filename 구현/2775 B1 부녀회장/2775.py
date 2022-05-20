T = int(input())

def count(floor, number):
  if floor == 0:
    return number
  elif number == 1:
    return 1
  return count(floor, number-1) + count(floor-1 , number)
  
  

for _ in range(T):
  floor = int(input())
  number = int(input())
  print(count(floor,number))
  