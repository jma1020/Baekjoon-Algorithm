inp = int(input())

line = 1
while inp > line:
  inp -= line
  line += 1

top = 0
under =0
if line % 2 ==0:
  top = inp
  under = line + 1 - inp
else:
  top = line +1 - inp
  under = inp

print("{0}/{1}".format(top,under))


# 거의 이미 있는 풀이 참고한 내용이다...