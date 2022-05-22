import sys

N = int(sys.stdin.readline())

inp = list(int(sys.stdin.readline())for i in range(N))

inp.sort()

for i in inp:
  print(i)