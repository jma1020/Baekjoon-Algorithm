
alpa = ["c=","c-","dz=","d-","lj","nj","s=","z="]

inp = input()

for i in alpa:
  if i in inp:
    inp = inp.replace(i,"*")




print(len(inp))
  
# replace를 아예 한글자에 쓸데없는 문자로 바꿔주고 length를 재면된다
# 또 if문도 그냥 없애도 되는거였구나..