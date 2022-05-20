n = int(input()) # 66
num = n
cnt = 0 # 사이클 수

while True:
  a = num//10 # 몫 6
  b = num % 10 # 나머지 6
  c = (a+b) % 10  # 6 + 6 = 1"4"
  num =(b *10) + c # 60 + 4 = 64

  cnt = cnt + 1 # 사이클 + 1
  if(num == n): 
    break

print(cnt)