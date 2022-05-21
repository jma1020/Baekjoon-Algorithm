inp = input()

def hansu(inp):
  count = 0
  if  int(inp) < 100:
    return inp
  else:
    count += 99
    for i in range(100,int(inp)+1):
   
      if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
        count+=1
    return count


print(hansu(inp))