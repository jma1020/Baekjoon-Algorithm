inp = input()

if int(inp) < 10:
  inp = inp +'0'
compare = int(inp)
sum = 0
y = 1
if inp == sum:
  print(1)
i = 0

def ff(sum,inp):
  sum = int(inp[0]) + int(inp[1])
  inp = inp[1] + str(sum)[-1]
  if compare != int(inp):
    ff(sum,inp)
  global i 
  i = i+1
  
ff(sum,inp)
print(i)

