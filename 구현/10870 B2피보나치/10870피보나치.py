n = 0 
n2 = 1
copy = 0

inp = int(input())
for i in range(inp):
  copy = n
  n = n2
  n2 += copy
print(n)
