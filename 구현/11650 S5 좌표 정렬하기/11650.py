N = int(input())

inp = [list(map(int,input().split())) for _ in range(N)]

def compare(i):
  return i[0], i[1]


inp.sort(key=compare)
for i in inp:
  print(i[0], i[1])