
alpa = ["c=","c-","dz=","d-","lj","nj","s=","z="]

inp = input()

count = 0
for i in alpa:
  if i in inp:
    print(i)
    inp = inp.replace(i,"*")
    print(inp)
    count += 1


print(inp)
print(count + len(inp))  
# 오류 nljj 입력시 lj빠지고 그다음에 남아있는 nj를 가져간다