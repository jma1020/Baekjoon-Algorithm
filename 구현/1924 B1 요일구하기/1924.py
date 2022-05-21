month, day = map(int,input().split())

total = 0
total = (month-1) * 31 + day
for i in range(1,month):
  if i == 4 or i == 6 or i ==9 or i == 11:
    total -= 1
  elif i == 2:
    total -= 3



def value(a):
  return {
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT",
    0: "SUN"
  }.get(a, "hello")

print(value(total %7))
