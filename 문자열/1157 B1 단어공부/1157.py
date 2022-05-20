inp = input().upper()

setinp = list(set(inp))

maxlist = []
for i in setinp:
  count = inp.count(i)
  maxlist.append(count)

if maxlist.count(max(maxlist)) > 1:
  print("?")
else:
  print(setinp[maxlist.index(max(maxlist))].upper())

  


