import sys

N = int(sys.stdin.readline())

ls = [0] * 10001

for _ in range(N):
  number = int(sys.stdin.readline())
  ls[number] = ls[number] +1

for i in range(10001):
  if ls[i] != 0:
    for _ in range(ls[i]):
      print(i)
