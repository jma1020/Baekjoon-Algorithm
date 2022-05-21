A = ['SUN','MON','TUE','WED','THU','FRI','SAT']
B = [31,28,31,30,31,30,31,31,30,31,30,31]

month, day = map(int,input().split())

total = 0
for i in range(0, month-1):
  total += B[i]

total = (total+day) % 7

print(A[total])
