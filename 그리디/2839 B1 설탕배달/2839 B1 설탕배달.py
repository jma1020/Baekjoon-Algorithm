
inp = int(input())

count = 0
while inp >= 0:
  if inp % 5 ==0:
    count += (inp // 5)
    print(count)
    break
  inp -= 3
  count +=1
else:
  print(-1)




