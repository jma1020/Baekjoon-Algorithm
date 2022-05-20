N = int(input())

number = list(map(int,input()[:N]))

sum = 0
for i in number:
  sum += i

print(sum)
