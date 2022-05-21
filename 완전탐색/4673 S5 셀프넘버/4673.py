number = set(range(1,10001))
nonself = set()

for i in range(1,10001):
  for j in str(i):
    i += int(j)
  nonself.add(i)

self = list(number-nonself)
self.sort()

for result in self:
  print(result)