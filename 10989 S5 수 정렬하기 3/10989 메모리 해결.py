import sys
input = sys.stdin.readline
num = int(input())
arr = [0]*10

for i in range(num):
  a = int(input())
  arr[a-1] += 1
  # print(arr)

for i in range(10001):
  if arr[i] != 0:
    for j in range(arr[i]):
      print(i)