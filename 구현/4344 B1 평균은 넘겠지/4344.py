C = int(input())

for _ in range(C):
  inp = list(map(int,input().split()))
  
  headcount = inp[0]
  inp = inp[1:]
  average = sum(inp)/headcount
  count = 0
  for i in inp:
    if i > average:
      count +=1
  print("{0:0.3f}%".format(count/headcount *100))
  


