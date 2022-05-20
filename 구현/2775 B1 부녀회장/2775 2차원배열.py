T = int(input())

for _ in range(T):
  floor = int(input())
  number = int(input())

  arr = [[0 for col in range(number)] for row in range(floor+1)]

  for a in range(1, number+1): # 0층
    arr[0][a-1] = a
  for forfloor in range(1, floor+1):
    for room in range(1,number+1):
      if room == 1:
        arr[forfloor][room] = 1
      else:
        arr[forfloor][room] = arr[forfloor][room-1] + arr[floor-1][room]

  print(arr[floor][number-1])