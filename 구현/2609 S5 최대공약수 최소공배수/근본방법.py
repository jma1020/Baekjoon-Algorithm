def gcm(a,b):

  gcm =  1

  for k in range(2,min(a,b)+1):
    while(a % k == 0) & (b % k == 0):
      a = a // k
      b = b // k
      gcm = gcm * k
      continue
  return gcm



print(gcm(60,48))