n = int(input())

a, b = 1,1 # 초기 좌표
plans = input().split()

x = [0, -1, 0 ,1]
y = [1, 0, -1, 0]
  # 동 북 서 남
  # 우 상 좌 하
move_types = ['R' , 'U', 'L', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = a + x[i]
      ny = b + y[i]

  if nx < 1 or ny <1 or nx > n or ny > n:
    continue
  a, b = nx, ny

print(a, b)