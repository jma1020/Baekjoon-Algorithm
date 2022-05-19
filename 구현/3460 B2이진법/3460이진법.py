
n = 11 
i = 0
while n != 0:
  if n % 2 == 1:
    print(i, end=" ")
  n //= 2
  i += 1

n=11
y=""
print("2진수")
while n>0:
    y=str(n%2)+y
    n//=2
print(y)

